# DONT'T FORGET TO RENAME THE FILE
#
# Import the functions you wrote for HW 4.
from leejeffrey_disjointsets import *


# Write a function to find the set of a given statistician.
def find_set_statistician(name):
    if name in edge.keys():
        #print(edge[name])
        #print(dic[str(find_set(edge[name]))][2])
        return dic[str(find_set(edge[name]))][2]
    else:
        #print('null')
        return 'None'
    
    
 # load the data
def main():
    filename = 'statisticiansA-M.txt'
    with open(filename, 'r') as file:
        read_strings = file.read().splitlines()
    
    # take only unique last names FYI
    stat_list = []
    for string in read_strings:
        stat_list.append(string.split(',')[0])
    stat_list = list(set(stat_list))
    stat_list.sort()
    #print(stat_list)
    label_list = range(0,len(stat_list),1)
    print(label_list)
    for i in range(len(label_list)):
        make_set(str(label_list[i]),stat_list[i])   # {  "a":   }
        edge[stat_list[i]]=str(label_list[i])
    #print()
#    #print(dic)
        
    edgefile = 'edge_list.dat'
    with open(edgefile, 'r') as file:
        read_edge = file.read().splitlines()
#    edge_list = {}
#    for i in range(len(read_edge)):
#        #print(read_edge[i].split(' '))
#        edge_list[(read_edge[i].split(' ')[0])]=(read_edge[i].split(' ')[1])
    edge_list = []
    for i in range(len(read_edge)):
        edge_list.append((read_edge[i].split(' ')[0],read_edge[i].split(' ')[1]))
    #print(edge_list)
    
    for i in range(len(edge_list)):
        union(edge_list[i][0],edge_list[i][1])
    
    #print(dic)
#    #print(dic)
######################################################################### 
#    visualize the result
#    for i  in label_list:
#        print('Element {0} has label {1}, '.format( dic[str(i)][2],i) +
#              'parent {0}, and representative '.format (dic[str(i)][0] ) +
#              '{0}.'.format(dic[str(find_set(str(i)))][0]))
        
        
    #print(edge)
    
# read in edges

# initialize nodes

# perform unions


# run test cases
    print(find_set_statistician('Blackwell'))
    print(find_set_statistician('Bottou'))
    print(find_set_statistician('Brad'))
    print(find_set_statistician('Breslow'))
    print(find_set_statistician('Wellner'))
    print(find_set_statistician('Laird'))
    print(find_set_statistician('Fisher'))
    print(find_set_statistician('Holmes'))
    
if __name__ == "__main__":
    main()