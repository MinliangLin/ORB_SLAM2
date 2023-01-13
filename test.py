import ctypes
import os.path as osp
dll = ctypes.CDLL(osp.realpath('lib/libORB_SLAM2.so'))
print(dll.mytest())
