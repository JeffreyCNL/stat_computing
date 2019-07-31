# author: Chia-Ning Lee
# implementing gaussain kernel and kernel density estimation
import numpy as np
import math

outFile = open('D:/Users/User/Documents/UW ME/stat534(statiscal computing)/hw/HW3/hw3-pb1-x.dat')
obs_data=np.loadtxt('hw3-pb1-x.dat') # load the data into numpy array
print(obs_data)

outFile = open('D:/Users/User/Documents/UW ME/stat534(statiscal computing)/hw/HW3/hw3-pb1-y.dat')
qry_data = np.loadtxt('hw3-pb1-y.dat')

n = len(obs_data) # 1000
m = len(qry_data) # 300

h = 0.1

def gaussian_kernel(z):
	return (math.exp(-(z**2)/2)) / (math.pow(math.pi*2, 0.5))

def kde(y):
	total = 0
	for x in obs_data:
		total += gaussian_kernel((y - x)/h)
	return total / n

if __name__ =='__main__':
	kde_list = []
	for y in qry_data:
		print(kde(y)) # f(yi), i = 1... m
