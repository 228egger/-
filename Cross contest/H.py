import sys
import random
random.seed('codeforces!!111!')
import queue



#For demo
#f = open("t0", "r")
#input = f.readline


def read_int():
    return int(input())


def read_array(sep=None, maxsplit=-1):
    return input().split(sep, maxsplit)

    
def read_int_list(sep=None, maxsplit=-1):
    return [int(x) for x in input().split(sep, maxsplit)]
    

def write(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in args) + end)


def write_array(array, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    sys.stdout.write(sep.join(str(a) for a in array) + end)




def parse(str):
    stack = []
    def apply_operation():
        b = stack.pop()
        op = stack.pop()
        a = stack.pop()
        if op == '+':
            stack.append(a + b)
        elif op == '-':
            stack.append(a - b)
        elif op == '*':
            stack.append(a * b)
    for value in str:
        if value.isdigit():
            stack.append(int(value))
        elif value in ['+', '-']:
            while len(stack) > 1 and stack[-2] in ['*', '-', '+']:
                apply_operation()
            stack.append(value)
        elif value == '*':
            stack.append(value)
        elif value == '(':
            stack.append(value)
        elif value == ')':
            while stack[-2] != '(':
                apply_operation()
            stack.pop(-2)
    while len(stack) > 1:
        apply_operation()

    
    return stack[0] % (10 ** 9 + 7)


n = read_int()
vars = read_array()

result = parse(vars)
write(int(result))