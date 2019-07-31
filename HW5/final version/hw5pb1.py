# Import the functions you wrote for HW 4.
# author: Chia-Ning Lee
# implementing disjoint and find the representative given edge list

import leejeffrey_disjointsets as ds
import clean as cl

# Write a function to find the set of a given statistician.
def find_set_statistician(name):

	filename = 'statisticiansA-M.txt'
	with open(filename, 'r') as file:
		read_strings = file.read().splitlines()

	# take only unique last names FYI
	stat_list = []
	for string in read_strings:
	    stat_list.append(string.split(',')[0])
	stat_list = list(set(stat_list)) # make a hash table
	stat_list.sort() # sort the name in order
	if name not in stat_list: # this will stop the function from forming the node when we discover the name is not even in the list
		return None

	label_list = []
	for label in stat_list:
		label_list.append(stat_list.index(label)) # give the names ID as label
		if label == name:
			input_index = stat_list.index(label) # get the name as index so that we can find it later

	# read in edges
	edge_list = []
	edgefile = 'edge_list.dat'
	with open(edgefile, 'r') as file:
		read_edge = file.read().splitlines()

	for i in range(len(read_edge)):
		# edge_list.append((read_edge[i].split(' '), read_edge[i].split(' ')))
		edge_list.append(tuple(map(int, read_edge[i].split(' ')))) # conver into int

	# edge_list = cl.make_edges(stat_list) # form the edge by the file.https://www.itread01.com/content/1544727607.html

	# initialize nodes
	stat_dict = {}
	for label in label_list:
		stat_dict[label] = ds.Node(label) # form a dict index as key, node as value


	# perform unions
	for edge in edge_list:
		node1 = stat_dict[edge[0]] # take out the node from the hash table a.k.a dict. O(1)
		node2 = stat_dict[edge[1]]
		ds.union(node1, node2)

	node = stat_dict[input_index]
	return stat_list[node.parent.label]
	# print('Element {0} has label {1},'.format(name, input_index) +
 #  	      ' parent is {0}, and representative is {1}'.format(node.parent.label, node.repr.label))

# run test cases
# find_set_statistician('Blackwell')
print(find_set_statistician('Blackwell'))
print(find_set_statistician('Bottou'))
print(find_set_statistician('Brad'))
print(find_set_statistician('Breslow'))
print(find_set_statistician('Wellner'))
print(find_set_statistician('Laird'))
print(find_set_statistician('Fisher'))
print(find_set_statistician('Holmes'))