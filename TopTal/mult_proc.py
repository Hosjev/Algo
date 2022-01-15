#!/usr/bin/python

"""Use multi-processing for CPU bound tasks and true parallelism (full code copy in memory for each process--GIL workaround)."""
import logging
import os
import sys
import time
from functools import partial
from multiprocessing.pool import Pool
curr_wd = "/home/hosjev/PythonPlay"
sys.path.append(curr_wd)
sys.path.append("/home/hosjev/.local/lib/python3.6/site-packages")
from TopTal.download import *
from Utilities.custlogging import py_logger

# Fire off all logging to file
tt_log = f"{curr_wd}/TopTal/all_msgs.log"
logger = py_logger(tt_log, "TopTal_multi")



def main():
    start_time = time.time()
    download_dir = setup_download_dir()
    links = get_links() # blocking
    download = partial(download_link, download_dir)
    with Pool(12) as p:
        p.map(download, links)
    dl_time = time.time()-start_time
    avg_time = float(dl_time)/len(links)
    logger.info(f"{len(links)} Imgur images downloaded in {dl_time}.")
    logger.info(f"Average time for download: {avg_time}.")


if __name__ == "__main__":
    main()
