# Threading procs and adding them to queue
import logging
import os
import sys
import time
from queue import Queue
from threading import Thread
curr_wd = "/home/wendiw/Xenial_Backup/PythonPlay"
sys.path.append(curr_wd)
from TopTal.download import *


# Fire off all logging to file
tt_log = f"{curr_wd}/TopTal/all_msgs.log"
logger = logging.getLogger("TopTal_threads")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(tt_log)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)



class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory, link = self.queue.get()
            try:
                download_link(directory, link)
            finally:
                self.queue.task_done()


def main():
    ts = time.time()
    download_dir = setup_download_dir()
    links = get_links()
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 4(5) worker threads
    for x in range(4):
        worker = DownloadWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    for link in links:
        logger.info(f"Queueing {link}")
        queue.put((download_dir, link))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    dl_time = time.time()-ts
    avg_time = float(dl_time)/len(links)
    logger.info(f"{len(links)} Imgur images downloaded in {dl_time}.")
    logger.info(f"Average time for download: {avg_time}.")


if __name__ == "__main__":
    main()
