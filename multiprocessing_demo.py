from multiprocessing import Process
from mywsgi import getLocalFileLogger

if __name__ == '__main__':
    def hello(msg="hello world"):
        print(msg)

    logger = getLocalFileLogger(path="./test.log")
    p = Process(target=logger.info,args=("Fuck You!World!",))
    p.start()
    p.join()
