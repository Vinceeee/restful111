def do_sth1(*args,**kargs):
    result = []
    if args:
        for arg in args:
            result.append(arg)
    if kargs:
        for k,v in kargs.items():
            result.append(v)
    return str(result)

def do_sth2(*args,**kargs):
    return "nothing left" 

def do_sth3(*args,**kargs):
    return "nothing left" 

if __name__ == '__main__':
    pass

    import requests # can use requests to do the testing , very fancy