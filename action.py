import time
from eventletTest import HandlerWSGI

app = HandlerWSGI(host="127.0.0.1")


@app.route("/")
def do_sth1(environ,start_response):

    # do some handling ...
    start_response('200 OK', [('Content-type', 'text/plain')])
    for i in range(10):
        time.sleep(0.2)
        print(i)
        yield "{0} -- hello world \n".format(str(i))


@app.route("/a1",methods="POST")
def do_sth2(*args, **kargs):

    start_response = kargs["start_response"]

    start_response('200 OK', [('Content-type', 'text/plain')])
    for i in range(10):
        time.sleep(0.2)
        print(i*10)
        yield "{0} -- hello world \n".format(str(i))


@app.route("/a2",methods=["GET","POST"])
def do_sth3(*args, **kargs):
    return "do_sth3: nothing left"


if __name__ == '__main__':
    app.run()
