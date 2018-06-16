#!/usr/bin/env python3.6

import logging
import logging.handlers
from logging.handlers import SysLogHandler

'''
python logging usage
more info could be found in https://docs.python.org/3.6/howto/logging-cookbook.html#context-info
'''

def logToMultiDest():
    # from https://docs.python.org/3.6/howto/logging-cookbook.html#context-info
    import logging

    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename='/tmp/myapp.log',
            filemode='a')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    # Now, we can log to the root logger, or any other logger. First the root...
    logging.info('Jackdaws love my big sphinx of quartz.')

    # Now, define a couple of other loggers which might represent areas in your
    # application:

    logger1 = logging.getLogger('myapp.area1')
    logger2 = logging.getLogger('myapp.area2')

    logger1.debug('Quick zephyrs blow, vexing daft Jim.')
    logger1.info('How quickly daft jumping zebras vex.')
    logger2.warning('Jail zesty vixen who grabbed pay from quack.')
    logger2.error('The five boxing wizards jump quickly.')


def getSysLogger():
    # this will log message into /var/log/message
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fmt = "[%(levelname)s] %(pathname)s %(message)s"
    formatter = logging.Formatter(fmt)
    handler = SysLogHandler(address="/dev/log")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def getLocalFileLogger():
    # this will log message into /var/log/message
    fmt = "WSGI - [%(levelname)s] %(pathname)s %(message)s"
    formatter = logging.Formatter(fmt)
#   handler = SysLogHandler(address="/dev/log",facility=SysLogHandler.LOG_LOCAL0)
    handler = logging.FileHandler("this.log")
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
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
#   getRotatingLogger()
    logToMultiDest()
