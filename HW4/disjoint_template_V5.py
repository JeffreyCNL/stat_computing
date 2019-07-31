# We define a class for the nodes of disjoint sets.
class Node:

    # The __init__ function defines the initial values of a new node.  The
    # label value must be passed to a new node as an argument.  We also add
    # the attributes parent and rank.
    def __init__(self, label):
        self.label = label
        self.parent = self
        self.rank = 0

    # def __contains__(self, label):
    #     if self.label:
    #         return True
        


# Next, we define some functions to works with our class.  We will start
# with a function to make a new set.
def make_set(node):

    # We set the parent of the node to itself since it is now in a set by
    # itself.  Note the use of the dot operator.
    node.parent = node
    rank = 0


# Now, we write a function to find the representative of a node.
def find_set(node): 
    if node != node.parent: # if the set is not the parent of its own
        node.parent = find_set(node.parent)
    return node.parent


# Next, we write a function that links the representatives of two sets.
def link(node1, node2):
    if node1.rank > node2.rank: # root with higher rank becomes the parent
        node2.parent = node1
        return node1
    else: # either smaller or equal
        node2.parent = node1 # arbitrary choose the root as the parent. In this case we chose y
        if node1.rank ==  node2.rank: # if the rank of two sets are the same
            node1.rank = node1.rank + 1 # union this two set will make the rank up by one
        return node1



# Finally, we add a function to join two sets.
def union(node1, node2): # ptr to two roots as input
    return link(find_set(node1), find_set(node2)) # link two set together

def find_parent(node):
    threshold = 1
    if node != node.parent:
        print('node: ',node.label)
        print('parent: ', node.parent.label)
        while threshold == 1:
            threshold += 1
            node.parent = find_parent(node.parent)
    return node.parent




# Now, we write our main function to run some test cases.
def main():
    # We import the string library for later (test cases).
    import string

    
    # This test case should look familiar.  It is a problem from the quiz.
    # First, we list all of the elements.
    label_list = list(string.ascii_lowercase[:8])

    # Then, we list the edges in the form of tuples.
    edge_list = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('b', 'c'), ('b', 'f'),
                 ('d', 'g')]

    # (1) Initialize nodes 
    nodes = []
    for label in label_list:
        nodes.append(Node(label))
    # print(nodes[0].label)
        # print(node)
    # (2) We build our sets based on the given edges.
    # label_list = []
    for edge in edge_list:
    # sequence of Union()
        node1 = 0
        node2 = 0
        while node1 ==0 or node2 ==0:
            for node in nodes:
                if (edge[0] == node.label):
                    node1 = node
                elif (edge[1] == node.label):
                    node2 = node
            union(node1, node2)
            # print("node1: ", node1.label)
            # print("node2: ", node2.label)



    # (3) We print our results. An example of printing

    # for node in nodes:
    #     # if node.label in label_list:
    #     if node.label == find_set(node).label:
    #         print('Element {0} has label {1},'.format(node.label, node.label) +
    #               ' it is root, and also representative {0}'.format(find_set(node).label))      
    #     else:
    #         print('Element {0} has label {1}, '.format(node.label, node.label) +
    #               'parent {0}, and representative '.format(find_parent(node).label) +
    #               '{0}.'.format(find_set(node).label))
    for node in nodes:
        print(node.label)
        find_parent(node)


# Run test cases as long as this isn't used as a module.
if __name__ == '__main__':
    main()