import random
import string

# clean the data
filename = 'statisticiansA-M.txt'
with open(filename, 'r') as file:
    read_strings = file.read().splitlines()

stat_list = []
for item in read_strings:
    stat_list.append(item.split(',')[0])

stat_list = list(set(stat_list))
stat_list.sort()

with open(filename, 'w') as file:
    for item in stat_list:
        file.write(item + '\n')


# make edge list
def make_edges(input_list):
    edge_list = []
    alph_list = list(string.ascii_uppercase[:13])
    start = 0
    stop = 0
    k = 0
    while k < len(alph_list):
        check = alph_list[k]
        while input_list[stop][0] == check:
            stop += 1
            if stop >= len(input_list):
                stop -= 1
                break
        stop += 1
        if start != (stop - 1):
            elements = list(range(start, stop))
            random.seed(7)
            random.shuffle(elements)
            for i in range(len(elements)-1):
                edge_list.append((elements[i], elements[i+1]))
        start = stop
        k += 1
    random.seed(5)
    random.shuffle(edge_list)
    return edge_list


edge_list = make_edges(stat_list)
# print(edge_list)
edge_file = 'edge_list.txt'
with open(edge_file, 'w') as file:
    file.write('\n'.join('%s %s' % edge for edge in edge_list))
