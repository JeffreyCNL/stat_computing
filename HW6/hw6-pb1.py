# Code from Chapter 14 of Machine Learning: An Algorithmic Perspective
# A simple Gibbs sampler
# author: Chia-Ning Lee
# implement gibbs sampling given neighbor list
import numpy as np
import matplotlib.pyplot as plt
import math

def clique_potential(xi, xj, J):
    if xi==xj:
        ksi = 1
    else:
        ksi = math.exp(-2*J)
    return ksi

def find_neighbor(arr, j):
    neighbor_lst = [(arr[1], arr[4]), 
                    (arr[0], arr[2], arr[5]),
                    (arr[1], arr[3], arr[6]),
                    (arr[2], arr[7]),
                    (arr[0], arr[5], arr[8]),
                    (arr[1], arr[4], arr[6], arr[9]),
                    (arr[2], arr[5], arr[7], arr[10]),
                    (arr[3], arr[6], arr[11]),
                    (arr[4], arr[9], arr[12]), 
                    (arr[5], arr[8], arr[10], arr[13]),
                    (arr[6], arr[9], arr[11], arr[14]),
                    (arr[7], arr[10], arr[15]),
                    (arr[8], arr[13]),
                    (arr[9], arr[12], arr[14]), 
                    (arr[10], arr[13], arr[15]),
                    (arr[11], arr[14])]
    return neighbor_lst[j]

def gibbs(N):
    k = 16 # 16 nodes for this specific Markov network
    J = 1 # defined
    # J = 0.2
    arr = np.ones(k, dtype = int)
    mean_lst = [] # mean of every iteration.
    mean_itr = []
    for _ in range(N): # iteration times
        # plot(arr)
        mean_lst.append(np.mean(arr[0:3], dtype = float)) # every iteration. compute the mean and store
        # print('mean', mean)
        for j in range(k): 
            num = 1
            den1 = 1
            den2 = 1
            neighbor = find_neighbor(arr, j)
            for i in range(len(neighbor)):
                decider = np.random.uniform(0, 1)
                num *= clique_potential(arr[j], neighbor[i], J)
                den1 *= clique_potential(arr[j], neighbor[i], J)
                den2 *= clique_potential(-arr[j], neighbor[i], J)
            den = den1 + den2
            p = num/den
            if p <= decider:
                arr[j] = 1
            elif p > decider:
                arr[j] = -1
        mean_itr.append(np.mean(mean_lst, dtype = float)) 
        # this will update the mean for every itr, and store it as vector so that can be plotted 
    total_mean = np.mean(mean_lst, dtype = float) 
    # from the store list, compute the total mean of all iteration,one scalar
    print('first three nodes mean after 100 iteration:', total_mean)
    return mean_itr

def plot(arr):
    dict = {1:'+', -1:'-'}
    for i in range(len(arr)):
        print(dict[arr[i]],end = "")
    print()

def jump_gibbs(N):
    grp1 = [0, 2, 5, 7, 8, 10, 13, 15]
    grp2 = [1, 3, 4, 6, 9, 11, 12, 14]
    k = 16 # 16 nodes for this specific Markov network
    J = 1 # defined
    # J = 0.2
    arr = np.ones(k, dtype = int)
    mean_lst = []
    mean_itr = []
    for _ in range(N): # iteration times
        # plot(arr)
        mean_lst.append(np.mean(arr[0:3], dtype = float))
        for j in range(len(grp1)): # sampling from group 1 first
            num = 1
            den1 = 1
            den2 = 1
            neighbor = find_neighbor(arr, grp1[j])
            for i in range(len(neighbor)):
                decider = np.random.uniform(0, 1)
                num *= clique_potential(arr[j], neighbor[i], J)
                den1 *= clique_potential(arr[j], neighbor[i], J)
                den2 *= clique_potential(-arr[j], neighbor[i], J)
            den = den1 + den2
            p = num/den
            if p <= decider:
                arr[grp1[j]] = 1
            elif p > decider:
                arr[grp1[j]] = -1

        for j in range(len(grp2)): # later sampling group 2
            num = 1
            den1 = 1
            den2 = 1
            neighbor = find_neighbor(arr, grp2[j])
            for i in range(len(neighbor)):
                decider = np.random.uniform(0, 1)
                num *= clique_potential(arr[j], neighbor[i], J)
                den1 *= clique_potential(arr[j], neighbor[i], J)
                den2 *= clique_potential(-arr[j], neighbor[i], J)
            den = den1 + den2
            p = num/den
            if p <= decider:
                arr[grp2[j]] = 1
            elif p > decider:
                arr[grp2[j]] = -1
        mean_itr.append(np.mean(mean_lst, dtype = float))
    total_mean = np.mean(mean_lst, dtype = float)
    print('first three nodes mean after 100 iteration:', total_mean)
    return mean_itr # can be used to plot

if __name__ =='__main__':
    mean_itr = gibbs(100)
    jump_mean_itr = jump_gibbs(100)

    x1 = np.arange(0,100)
    plt.figure()
    plt.plot(x1, mean_itr, color = 'r', label = 'normal sampling')
    plt.plot(x1, jump_mean_itr, color = 'b', label = 'jumping sampling')
    plt.xlabel('iteration times')
    plt.ylabel('mean')
    plt.title('J = 1')
    plt.legend()
    plt.show()


###### failure code
# def find_neighbor(row, col, mat):
#     n = int(math.sqrt(N))
    
#     if row == 0:
#         if col == 0:
#             # neighbor = neighbor[0], neighbor[2]
#             neighbor = mat[row+1][col], mat[row][col+1]
#         if col == n-1:
#             # neighbor = neighbor[0], neighbor[3]
#             neighbor = mat[row+1][col], mat[row][col-1]
#         if col > 0 and col < n-1:
#             # neighbor = neighbor[0], neighbor[2:]
#             neighbor = mat[row+1][col], mat[row][col+1], mat[row][col-1]
#     if row == n-1:
#         if col == 0:
#             # neighbor = neighbor[1:3]
#             neighbor =  mat[row-1][col], mat[row][col+1]
#         if col == n-1:
#             # neighbor = neighbor[1], neighbor[3]
#             neighbor =  mat[row-1][col], mat[row][col-1]
#         if col > 0 and col < n-1:
#             # neighbor = neighbor[1:]
#             neighbor =  mat[row-1][col], mat[row][col+1], mat[row][col-1]
#     if col == 0 and row != 0 and row != n-1:
#         neighbor = mat[row+1][col], mat[row-1][col], mat[row][col+1]
#     if col == n-1 and row != 0 and row != n-1:
#         neighbor = mat[row+1][col], mat[row-1][col], mat[row][col-1]
#     if (row > 0 and col > 0 and row < n-1 and col < n-1):
#         neighbor = mat[row+1][col], mat[row-1][col], mat[row][col+1], mat[row][col-1]
#     return neighbor

# def sample_with_neighbor(origin, neighbor):
#     n = len(neighbor)
#     for i in range(1, n):
#         num = clique_potential(origin, neighbor[0], J)
#         num *= clique_potential(origin, neighbor[i], J)
#         den = clique_potential(origin, neighbor[0], J)
#         den += clique_potential(origin, neighbor[i], J)
#     return num/den
