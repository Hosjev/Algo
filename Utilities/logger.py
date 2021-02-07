import time


def write_to_log(log_file, msg):
    with open(f"{log_file}", "a", encoding="utf-8") as lf:
        lf.write(time.asctime() + "--" + msg + "\n")
        lf.close()

def read_from_log(log):
    pass
