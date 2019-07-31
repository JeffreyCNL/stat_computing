import numpy as np
import itertools
import scipy.stats as ss

seql = 'AABCABC'
seq = ['AABCABC']

xid = np.argwhere([[0,0],[0,1],[2,1]]).flatten() #.item()
print(xid)
# yid = xid + 1
# print(yid)
# T = 7
# yid = yid[yid < T]
# print(yid)

# for x, y in itertools.product(range(3), repeat=2):
# 	print('x:', x)
# 	print('y:', y)
p = np.unique(seq)
print(p)
p = []
# _os = self.obs_seq if obs_seq is None else np.array(list(obs_seq))
_os = p if p is None else np.array(list(p))
print(_os)

t1 = np.array([[1,2,3],[4,5,6]])
print(t1)
t1 = t1[:,1]
print(t1)
# for x, y in itertools.product(range(K), repeat=2): # nested for loop
#     xid = np.argwhere(seql == states[x]).flatten() # return an array collapsed into 1D
#     yid = xid + 1
#     yid = yid[yid < T]
#     s = np.count_nonzero(seql[yid] == states[y])
#     matrix[x, y] = s