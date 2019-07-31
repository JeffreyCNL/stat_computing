import numpy as np
import urllib
import time

from six.moves.urllib.request import urlopen

link = "https://www.stat.washington.edu/mmp/courses/stat534/spring19/Assignments/statisticiansA-M.txt"
f = urlopen(link)
myfile = f.readlines()
# open('myfile', 'r', encoding='utf-8')
ll0 = b''.join(myfile).decode('utf-8')
# ll0.strip(' ')
ll0 = ll0.split('\n')
while '' in ll0:
	ll0.remove('')
n = len(ll0)
t = 100
k = 3
print(ll0)
# print(n)

############## b ################
truncate_str = []
for line in ll0:
	# print(line[0:3])
	truncate_str.append(line[0:k])
# print(truncate_str)

############### c ################
longstring = []
for strings in truncate_str:
	longstring.append(strings)
len_longstr = len(longstring)
# print(longstring)
# print(ll0 == longstring)
# print(len(longstring))

#################### d ######################
no_pre_alloc_start = time.perf_counter()
longlongstring = []
for i in range(t):
	for line in longstring:
		longlongstring.append(line)
no_pre_alloc_end = time.perf_counter()

no_pre_alloc_runtime = no_pre_alloc_end - no_pre_alloc_start
print("(d)Non-preallocate runtime: ", no_pre_alloc_runtime)

length = len(longlongstring)

################ e ######################
pre_alloc_start = time.perf_counter()
dt = np.dtype('<U' + str(k))
arr = np.empty(len_longstr, dtype = dt)

for j in range(len(longstring)):
	arr[j] = longstring[j]
arr = np.tile(arr, t)     # copy arr t times and save it as arr.
pre_alloc_end = time.perf_counter()
# print(arr)
pre_alloc_runtime = pre_alloc_end - pre_alloc_start
print("(e)Preallocate runtime: ", pre_alloc_runtime)

# print('longstring == arr? {0}'.format( longlongstring == arr))

############### g ###################
# print(longstring)
# print(longlongstring)
