import ctypes
import os


# Try to locate the .so file in the same directory as this file
def _load_mod():
    #   _pwd = "/home/vagrant/restful111/clib"
    _pwd = os.path.abspath(".")
    _file = os.path.join(_pwd, "clib/libsample.so")
    _mod = ctypes.cdll.LoadLibrary(_file)
    return _mod


def testLong():
    a = ctypes.c_longlong(2**35)
    _mod = _load_mod()
    testInt = _mod.testInt
    testInt.argtype = ctypes.c_longlong
    testInt.restype = ctypes.c_voidp
    print(a)
    testInt(a)


def fib(n):
    n = ctypes.c_uint(n)
    _mod = _load_mod()
    _fib = _mod.fib
    _fib.argtype = ctypes.c_uint
    _fib.restype = ctypes.c_longlong
    result = _fib(n)
    return result


def doSth(n):
    _mod = _load_mod()
    _mod = _load_mod()
    dosth = _mod.some_wasting_time_op
    dosth.argtype = ctypes.c_int
    dosth.restype = ctypes.c_char_p
    return dosth(n)


if __name__ == '__main__':
    #   testLong()
    #   print("Fib 100 --> {}".format(fib(100)))
    doSth(1)
