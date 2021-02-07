import time
import sys
from pathlib import Path
from PIL import Image
from functools import partial
from concurrent.futures import ProcessPoolExecutor
curr_wd = "/home/wendiw/Xenial_Backup/PythonPlay"
sys.path.append(curr_wd)
from Utilities.custlogging import py_logger
from TopTal.download import *

# Fire off all logging to file
tt_log = curr_wd + "/TopTal/all_msgs.log"
logger = py_logger(tt_log, "TopTal_multi")



def create_thumbnail(size, path):
    """
    Creates a thumbnail of an image with the same name as image but with
    _thumbnail appended before the extension.  E.g.:

    >>> create_thumbnail((128, 128), 'image.jpg')

    A new thumbnail image is created with the name image_thumbnail.jpg

    :param size: A tuple of the width and height of the image
    :param path: The path to the image file
    :return: None
    """
    image = Image.open(path)
    image.thumbnail(size)
    path = Path(path) # From POSIX object strip and combo create filename
    name = path.stem + '_thumbnail' + path.suffix
    thumbnail_path = path.with_name(name)
    image.save(thumbnail_path)

def main():
    logger.info("Starting thumbnail creation...")
    ts = time.time()
    # Partially apply the create_thumbnail method, setting the size to 128x128
    # and returning a function of a single argument.
    thumbnail_128 = partial(create_thumbnail, (128, 128))

    # Create the executor in a with block so shutdown is called when the block
    # is exited.
    with ProcessPoolExecutor(4) as executor:
        executor.map(thumbnail_128, Path(curr_wd + "/TopTal/images/thumbnails").iterdir())
    logger.info("Took", time.time() - ts)


if __name__ == "__main__":
    main()
