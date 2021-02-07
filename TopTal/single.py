import os
import sys
import time
import logging
curr_wd = "/home/wendiw/Xenial_Backup/PythonPlay"
sys.path.append(curr_wd)
from Utilities.custlogging import py_logger
from TopTal.download import *

# Fire off all logging to file
tt_log = f"{curr_wd}/TopTal/all_msgs.log"
logger = py_logger(tt_log, "TopTal_multi")


def main():
    ts = time.time()
    download_dir = setup_download_dir()
    links = get_links()
    for link in links:
        download_link(download_dir, link)
    dl_time = time.time()-ts
    avg_time = float(dl_time)/len(links)
    logger.info(f"{len(links)} Imgur images downloaded in {dl_time}.")
    logger.info(f"Average time for download: {avg_time}.")

if __name__ == "__main__":
    main()
