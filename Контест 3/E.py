import sys
input = sys.stdin.buffer.readline
import random

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


class SegTreeNode:  
    def __init__(self, idx, count = 0):
        self.idx = idx # index in a
        self.count = count
        self.leftmost = None
        self.rightmost = None
        
    def __str__(self):
        return f"(idx={self.idx}, max={self.max})"

    def __repr__(self):
        return f"(idx={self.idx}, max={self.max})"
    

class SegTree:
    def __init__(self, inp: list):
        self.inp = inp
        self.a = []
        n = len(inp)
        m = 1 # min(power of 2) ≥ n 
        h = 0 # height of the tree
        while m < n:
            h += 1
            m *= 2
        
        self.total_length = 2**(h+1)-1
        self.a = [None] * self.total_length
        self.fst = self.total_length - m # index of first element of the input in a
        fst = self.fst
        
        for i, max in enumerate(inp):
            self.a[fst+i] = SegTreeNode(fst+i, 0)
            self.a[fst+i].leftmost = i
            self.a[fst+i].rightmost = i
            
        for i in range(fst+n, self.total_length):
            self.a[i] = SegTreeNode(i, -float("inf"))
            self.a[i].leftmost = i
            self.a[i].rightmost = i
            
        for i in range(fst-1, -1, -1):
            left = self.a[self.left(i)]
            right = self.a[self.right(i)]
            self.a[i] = SegTreeNode(i, 0)
            self.a[i].leftmost = left.leftmost
            self.a[i].rightmost = right.rightmost
    
    def update(self, l, r, idx = 0):
        if idx >= len(self.a):
            return
        if l <= self.a[idx].leftmost and self.a[idx].rightmost <= r:
            self.a[idx].count += 1
            return
        if self.a[idx].leftmost > r or self.a[idx].rightmost < l:
            return
        self.update(l, r, self.left(idx))
        self.update(l, r, self.right(idx))

    def __call__(self, l, r, idx = 0):
        if idx >= len(self.a):
            return 0
        if self.a[idx].leftmost > r or self.a[idx].rightmost < l:
            return 0
        if (l <= self.a[idx].leftmost and self.a[idx].rightmost <= r):
            return self.a[idx].count
        return self(l, r, self.left(idx)) + self(l, r, self.right(idx)) + self.a[idx].count

    def fin_arr(self):
        return sorted(self.a[self.fst:len(self.inp) + self.fst], reverse=True, key = lambda x: x.count)






    def parent(self, idx): # Если нумерация с единицы: parent(idx) = idx // 2
        p = (idx + 1) // 2 - 1
        return p if p >= 0 else None
        
    def left(self, idx):
        c = (idx + 1) * 2 - 1
        return c if c < len(self.a) else None
    
    def right(self, idx):
        c = (idx + 1) * 2 
        return c if c < len(self.a) else None


n, k = map(int, read_array())
rmq = SegTree([0 for _ in range(n)])
arr = read_int_list()
arr = sorted(arr, reverse=True)
for _ in range(k):
    l, r = map(int, read_array())
    l, r, = l-1, r-1
    rmq.update(l, r, 0)
arr_rates = sorted([rmq(i, i) for i in range(n)], reverse=True)
summa = 0
for i in range(n):
    summa += arr[i] * arr_rates[i]
write(summa)