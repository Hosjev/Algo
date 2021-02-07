import logging
import os
import sys
import time
from redis import Redis
from rq import Queue
curr_wd = "/home/wendiw/Xenial_Backup/PythonPlay"
sys.path.append(curr_wd)
from TopTal.download import *
from Utilities.custlogging import py_logger

# Fire off all logging to file
tt_log = f"{curr_wd}/TopTal/all_msgs.log"
logger = py_logger(tt_log, "TopTal_multi")


def main():
    download_dir = setup_download_dir()
    links = get_links()
    q = Queue(connection=Redis(host='localhost', port=6379))
    for link in links:
        q.enqueue(download_link, download_dir, link)

if __name__ == '__main__':
    main()
