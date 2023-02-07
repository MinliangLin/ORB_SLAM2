from lib.ORB_SLAM2 import static_inc, test_size
import numpy as np

assert static_inc() == 2
assert static_inc() == 3

dat = np.eye(4) * 7
assert test_size(dat) == 16

print('passed test')
