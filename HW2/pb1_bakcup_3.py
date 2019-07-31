import sys
import argparse


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--inputdata', type=str,
        help='input a string for me to operate')
    return parser

def expr(arr):
    op = '+-*/'
    stack =[]
    while(len(arr)!=0):
        for i in range(len(arr)):
            if arr[i] not in op:
                stack.append(int(arr.pop(i)))
                break
            elif arr[i] in op:
                if (arr[i] =='+'):
                    temp2=stack.pop()
                    temp1=stack.pop()
                    arr.pop(i)
                    stack.append(temp1+temp2)
                    break
                elif (arr[i] =='-'):
                    temp2=stack.pop()
                    temp1=stack.pop()
                    arr.pop(i)
                    stack.append(temp1-temp2)
                    break
                elif (arr[i] =='*'):
                    temp2=stack.pop()
                    temp1=stack.pop()
                    arr.pop(i)
                    stack.append(temp1*temp2)
                    break
                elif (arr[i] =='/'):
                    temp2=stack.pop()
                    temp1=stack.pop()
                    arr.pop(i)
                    stack.append(temp1/temp2)
                    break
                else:
                    pass
            else:
                pass
                #raise ValueError('This opeation I don't know')
    print(stack[0])


if __name__ == '__main__':
        args = setup_parser().parse_args()
        print('My input is :', args.inputdata)
        str_arr = args.inputdata;

        print(str_arr)
        arr =[]
        for i in range(len(str_arr)):
            arr.append(str_arr[i])
        print(arr)
        expr(arr)

                
                    