#!/usr/bin/env python

import logging
import logging.handlers
from logging.handlers import SysLogHandler
'''
python logging usage
more info could be found in https://docs.python.org/3.6/howto/logging-cookbook.html#context-info
'''


def getSysLogger():
    # this will log message into /var/log/message
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fmt = "[%(levelname)s] %(pathname)s %(message)s"
    formatter = logging.Formatter(fmt)
    handler = SysLogHandler(address="/tmp/log")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def getLocalFileLogger(path="/tmp/app.log", level=logging.INFO):
    fmt = "%(asctime)8s WSGI(%(process)s) - [%(levelname)s] %(filename)s %(message)s"
    # this will log message into /var/log/message
    formatter = logging.Formatter(fmt)
    handler = logging.FileHandler(path)
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.setLevel(level)
    return logger

def getRotatingLogger():
    import glob
    LOG_FILENAME = 'logging_rotatingfile_example.out'

    # Set up a specific logger with our desired output level
    my_logger = logging.getLogger('MyLogger')
    my_logger.setLevel(logging.DEBUG)

    fmt = "[%(levelname)s] %(pathname)s %(message)s"
    formatter = logging.Formatter(fmt)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=20, backupCount=5)
    handler.setFormatter(formatter)

    my_logger.addHandler(handler)

    # Log some messages
    for i in range(20):
        my_logger.debug('i = %d' % i)

        # See what files are created
        logfiles = glob.glob('%s*' % LOG_FILENAME)

        for filename in logfiles:
            print(filename)


def main():
    #   logger = getLocalFileLogger()
    logger = getSysLogger()
    logger.debug("this is a debug test")
    logger.info("this is a info test")
    logger.error("this is a error test")
    logger.critical("this is a critical test")


if __name__ == '__main__':
    logger = getLocalFileLogger()
    logger.info("sdfasdfasd")
    pass
