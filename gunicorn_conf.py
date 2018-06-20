import multiprocessing

bind = "127.0.0.1:10618"
workers = multiprocessing.cpu_count() *2 + 1
worker_class = "eventlet"
threads = 4
# LOGGING
accesslog = "access.log"
errorlog = "error.log"
#loglevel = "debug"
# DEVELOP ONLY
reload = True
# BELOW CONFIGS ARE ONLY FOR TESTING
timeout = 10 # try to restart the workers
graceful_timeout = 10 # force to restart the workers
