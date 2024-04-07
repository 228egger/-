import sys
input = sys.stdin.buffer.readline
import random
random.seed('codeforces!!111!')


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


def get_stat(BITTree, k): 
    result = 0
    while (k > 0):
      while ((result | (result + 1)) < len(BITTree) and BITTree[result | (result + 1)] < k):
        result = (result | (result + 1))
      if (len(BITTree) <= result):
        return 0
      k -= BITTree[result]
      result += 1
    return result
	


def updatebit(BITTree, i ,v): 
    i -= 1
    while i < len(BITTree): 
        BITTree[i] += v 
        i = i | (i + 1) 

def construct(arr, n): 
	BITTree = [0]*(n+1) 
	for i in range(n): 
		updatebit(BITTree, arr[i], 1) 
	return BITTree 


n, q = map(int, read_array())
arr = read_int_list()
t = construct(arr, n)
questions = read_int_list()
for question in questions:
    if question > 0:
        updatebit(t, abs(question), 1)
    else:
        res = get_stat(t, abs(question))
        updatebit(t, res, -1)


print(get_stat(t, 1))

# This code is contributed by Raju Varshney 
