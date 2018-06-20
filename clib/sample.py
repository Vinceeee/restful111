import ctypes
import os

# Try to locate the .so file in the same directory as this file
def _load_mod():
    _pwd = "/home/vagrant/restful111/clib"
    _file = os.path.join(_pwd,"libsample.so")
    _mod = ctypes.cdll.LoadLibrary(_file)
    return _mod

# void looping()
def looping():
    _mod = _load_mod()
    looping = _mod.looping
    looping.argtype = ctypes.c_voidp
    looping.restype = ctypes.c_voidp
    looping()

# void mysleep(int)
def mysleep(sleep_time):
    _mod = _load_mod()
    mysleep = _mod.mysleep
    mysleep.argtype = ctypes.c_int
    mysleep.restype = ctypes.c_voidp
    mysleep(sleep_time)

if __name__ == '__main__':
    looping()
#   mysleep(2)
