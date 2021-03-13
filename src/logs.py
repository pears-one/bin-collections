import logging
import os
import json


def init():
    logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
    logfmt = json.dumps({
        "time": '%(asctime)s',
        "message": '%(message)s',
        "level": '%(levelname)s',
        "function": '%(filename)s.%(funcName)s',
        "logger": '%(name)s'
    })
    logging.basicConfig(filename=os.environ['LOG_FILE'], level=logging.DEBUG, format=logfmt)
