import sys
import operator

list_expr = []
for i in range(10):
	# print(i)
	list_expr.append(i)
# print(list_expr)

ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
stack = ['3','2','*']
print(stack[0].isdigit())
print(ops[stack[2]](float(stack.pop(0)),float(stack.pop(0))))
# print(ops['/'](2,2))
# print(list_expr.pop(len(list_expr)-1)) # always pop the last one.
# for i in range(3):
# 	print(list_expr.pop(0))



	# print("This is what I put in", sys.argv[i])
	# print("len of input", len(sys.argv) - 1)


# print(ops['+'](1,1))
# test = 2 operator_smbl('+') 3


# def main(argv):
# 	inputfile = ''
# 	outputfile = ''

# if __name__ = 'main':
# 	main(sys.argv[1:])
# class node:
# 	def __init__(self, data):
# 		self.left = None
# 		self.right = None
# 		self.data = data
# 	def insert(self, data):
# 		if self.data:
for i in range(len(sys.argv)):
	if (sys.argv[i] == '+' or sys.argv[i] == '-' or sys.argv[i] == '*' or sys.argv[i] == '/'):
		print('oh yeah!')

# class Node:

#     def __init__(self, data):

#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, data):
# # Compare the new value with the parent node
#         if self.data:
#             if data == '+' or data == '-' or data == '*' or data == '/':
#                 if self.left is None:
#                     self.left = Node(data)
#                 elif self.right is None:
#                     self.right = Node(data)
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()			

# root = Node(sys.argv[1])
# for i in range(1,len(sys.argv) - 1):
# 	root.insert(sys.argv[i])
# # root = Node(12)
# # root.insert(6)
# # root.insert(8)
# # root.insert(19)
# # root.insert(29)
# root.PrintTree()
string = '1.5'
string = float(string)
print(string.isdigit())





