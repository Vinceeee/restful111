import re
import six
import time
from mywsgi import MyWSGI
from clib.sample import mysleep,looping

app = MyWSGI(host="127.0.0.1",port=10618)

if six.PY3:
    xrange = range

@app.route("/")
def do_sth1(environ,start_response):
    # do some handling ...
    start_response('200 OK', [('Content-type', 'text/plain')])
    for i in xrange(999): # for python 2 , range will return a list instead of iterable , which waste memory a lot , but xrange is fine ^_^
        yield b"010"

@app.route("/a")
def do_a(environ,start_response):
    from datetime import datetime
    sleeps = 5 # by default 5 seconds
    if "QUERY_STRING" in environ:
        sleeps = re.findall("sleeps=(\d{1,3})",environ.get("QUERY_STRING")) 
        sleeps = int(sleeps[0]) if sleeps else 5
    mysleep(sleeps)
    start_response('200 OK', [('Content-type', 'text/plain')])
    resp = "{0} - aaabbbccc".format(str(datetime.now()))
    app.logger.info(resp)
#   yield bytes(resp.encode('utf8'))
    yield resp

@app.route("/looping")
def do_loop(environ,start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    looping()
    yield u""

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
    start_response = kargs["start_response"]
    start_response('200 OK', [('Content-type', 'text/plain')])
    return "do_sth3: nothing left"

if __name__ == '__main__':
    app.run()
