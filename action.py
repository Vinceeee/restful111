from eventletTest import HandlerWSGI

app = HandlerWSGI(host="127.0.0.1")


@app.route("/")
def do_sth1(*args, **kargs):
    result = []
    if args:
        for arg in args:
            result.append(arg)
    if kargs:
        for k, v in kargs.items():
            result.append(v)
    return "do_sth1: " + str(result)


@app.route("/a1",methods="POST")
def do_sth2(*args, **kargs):
    return "do_sth2 nothing left"


@app.route("/a2",methods=["GET","POST"])
def do_sth3(*args, **kargs):
    return "do_sth3: nothing left"


if __name__ == '__main__':
    app.run()
