import os.path as osp
from lib.ORB_SLAM2 import mytest

assert mytest() == 2
assert mytest() == 3
print('passed test')
