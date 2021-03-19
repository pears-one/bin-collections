import logging
import os
import json


def init(live: bool):
    logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
    logging.getLogger("twilio.http_client").setLevel(logging.WARNING)
    logfmt = json.dumps({
        "time": '%(asctime)s',
        "message": '%(message)s',
        "level": '%(levelname)s',
        "function": '%(filename)s.%(funcName)s',
        "logger": '%(name)s',
        "env": "live" if live else "dev"
    })
    logging.basicConfig(filename=os.environ['LOG_FILE'], level=logging.DEBUG, format=logfmt)
