import ctypes
import os.path as osp
dll = ctypes.CDLL(osp.realpath('lib/libORB_SLAM2.so'))
assert dll.mytest() == 2
assert dll.mytest() == 3
print('passed test')
