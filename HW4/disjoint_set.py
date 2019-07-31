
class disjoint_set(object):
	"""docstring for disjoint_set"""

	def __init__(self):
		self.rank = []
		self.parent = []
		self.sets = []
	
	def make_set(self, x):
		self.sets.append(x)
		self.parent.append(x) # Initialize the set. It itself is the parent.
		self.rank.append(0)

	def union(x, y): # ptr to two roots as input
		link(find_set(x), find_set(y)) # link two set together

	def link(x, y):
		if rank[x] > rank[y]: # root with higher rank becomes the parent
			parent[y] = x
		else: # either smaller or equal
			parent[x] = y # arbitrary choose the root as the parent. In this case we chose y.
			if rank[x] == rank[y]: # if the rank of two sets are the same
				rank[y] = rank[y] + 1 # union this two set will make the rank up by one

	def find_set(x):
		if x != parent[x]: # if the set is not the parent of its own
			parent[x] = find_set(parent[x])
		return parent[x]

	# def main():





if __name__ == '__main__':
	obj = disjoint_set()
	a = obj.make_set(1)
	b = obj.make_set(2)
	obj.union(a,b)
	# obj.main()
	# print(obj.make_set(1))
	# x = [1,2]
	# y = [2,3]
	# obj.union(x)
	# print(disjoint_set([2]))
	# make_set(1