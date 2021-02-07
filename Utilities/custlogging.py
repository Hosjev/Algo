import time
import logging


def write_to_log(log_file, msg):
    with open(log_file, "a", encoding="utf-8") as lf:
        lf.write(time.asctime() + "--" + msg + "\n")

def read_from_log(log):
    pass


def py_logger(log_fileh, log_name):
    """
    Instantiate logger object using Python's logging mod.
    Provide log file name and logger namespace name, eg:

    >>> py_logger("/var/log/my_app.log", "My_app_threading")
    
    :param log_fileh: (str) the dir/name of the log file
    :param log_name: (str) the logging namespace
    Note "log_name" has no spaces. Also, the namespace can
    be linked to called functions or classes within the
    main module. IE-"My_app_threading.aux_function"
    >Returns logging object.
    """
    #tt_log = f"{curr_wd}/TopTal/all_msgs.log"
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_fileh)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
