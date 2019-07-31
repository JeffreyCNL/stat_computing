# this script is tested by python3.7
# author Chia-Ning Lee
# an exercise to operate expr operation
# which is a reverse polish expression entered as a command line
# eg. expr 3 4 + evaluates 3+4 = 7
# 	expr 3 4 + 2 * evaluates (3+4)*2 = 14
# 	expr 2 3 4 + * evaluates 2*(3+4) = 14
import sys
import operator

def isnumber(aString):
	try:
		float(aString)
		return True
	except:
		return False

def error_checking(argc):
	if argc == 0:
		print("There is no input to compute!!")
		return 1
	elif argc > 1024:
		print("Too many input argument for stack!!")
		return 1

def expr(argc,argv):
	ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	stack = []
	for i in range(1, argc + 1): # start from 1 since argv[0] is hw2-expr.py
		if isnumber(sys.argv[i]): # if it's number, we will put it into the stack
			stack.append(sys.argv[i]) # in python use append as push
		else:
			if sys.argv[i] == '+' or sys.argv[i] == '*':
				stack.append(ops[sys.argv[i]](float(stack.pop()),float(stack.pop())))
				# operate the number by taking the symbol from the dict.
			if sys.argv[i] == '-' or sys.argv[i] == '/':
				num = float(stack.pop()) # minus and divide do not have commutative property
				stack.append(ops[sys.argv[i]](float(stack.pop()),num))
	if len(stack) > 1:  # another error checking whether there exists more than one member left in the stack
		print("Check if lack of operator, or too many numbers inserted")
		return sys.exit()
	else:
		return stack

if __name__ =='__main__':
	argc = (len(sys.argv) - 1)
	if error_checking(argc) == 1:
		print("You may want to fix the above error!")
	else:
		print(expr(argc, sys.argv).pop())
