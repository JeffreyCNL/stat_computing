import sys
import operator

class expr:
	ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	argc = len(sys.argv) - 1
	def error_checking(argc):
		if argc == 0:
			print("There is no input to compute!!")
		elif argc > 1024:
			print("Too many input argument for stack!!")

	def __init__(self,argc,sys.argv):
		ans = []
		while argc > 0:
			for i in range(1, argc):
				if argv[i].isdigit():
					ans.append(argv[i])
				else:
					if argv[i] == '+' or argv[i] == '*':
						ans.append(ops[argv[i]](pop(),pop()))
					if argv[i] == '-' or argv[i] == '/':
						num = pop()
						ans.append(ops[argv[i]](pop(),num))
		return ans

x = expr()

