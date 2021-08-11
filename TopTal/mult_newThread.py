"""Use threading for IO bound tasks knowing the GIL is being used."""
import logging
import os
import sys
import time
from functools import partial
from concurrent.futures import ThreadPoolExecutor
curr_wd = "/home/wendiw/Xenial/PythonPlay"
sys.path.append(curr_wd)
from Utilities.custlogging import py_logger
from download import *

# Fire off all logging to file
tt_log = f"{curr_wd}/TopTal/all_msgs.log"
logger = py_logger(tt_log, "TopTal_multi")



def main():
    start_time = time.time()
    download_dir = setup_download_dir()
    links = get_links()
    # By placing the executor inside a with block, the executors shutdown method
    # will be called cleaning up threads.
    # 
    # By default, the executor sets number of workers to 5 times the number of
    # CPUs.
    with ThreadPoolExecutor() as executor:

        # Create a new partially applied function that stores the directory
        # argument.
        # 
        # This allows the download_link function that normally takes two
        # arguments to work with the map function that expects a function of a
        # single argument.
        dn = partial(download_link, download_dir)

        # Executes fn concurrently using threads on the links iterable. The
        # timeout is for the entire process, not a single call, so downloading
        # all images must complete within X seconds.
        executor.map(dn, links, timeout=60)

    dl_time = time.time()-start_time
    avg_time = float(dl_time)/len(links)
    logger.info(f"{len(links)} Imgur images downloaded in {dl_time}.")
    logger.info(f"Average time for download: {avg_time}.")


if __name__ == "__main__":
    main()
