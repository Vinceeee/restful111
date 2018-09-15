import ctypes
import os

# Try to locate the .so file in the same directory as this file
def _load_mod():
#   _pwd = "/home/vagrant/restful111/clib"
    _pwd = "."
    _file = os.path.join(_pwd,"libsample.so")
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

if __name__ == '__main__':
#   looping()
#   mysleep(2)
    testLong()
