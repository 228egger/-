#!/usr/bin/env python3
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


class TreapNode:
    def __init__(self, value, prior):
        self.key = 1
        self.value = value
        self.prior = prior
        self._left = None
        self._right = None
        self._parent = None
    
    def update_data(self):
        self.key = sum(node.key for node in self.children) + 1
        
    # T.left = T_1
    @property
    def children(self):
        if self.left:
            yield self.left
        if self.right:
            yield self.right
    
    @property
    def left(self):
        return self._left
        
    @left.setter
    def left(self, l):
        self._left = l
        if l is not None:
            l._parent = self
            
    @property
    def right(self):
        return self._right
        
    @right.setter
    def right(self, r):
        self._right = r
        if r is not None:
            r._parent = self
            
    
    @property
    def parent(self):
        return self._parent
        
    def __str__(self):
        return f"({self.key}, {self.prior})"
        
    def _print(self):
        print(self, self.left, self.right)
        if self.left is not None:
            self.left._print()
        if self.right is not None:
            self.right._print()
        
    
class Treap:
    def __init__(self, key=None, prior=None, node_class=TreapNode):   
        self.nodes = []
        self.node_class = node_class
        if key is None:
            assert prior is None
            self.root = None
        else:
            self.root = node_class(key, prior)
            self.nodes.append(self.root)
        

    def __len__(self):
        if self.root is None:
            return 0
        return self.root.key
            
    def insert(self, value, prior):
        node = self.node_class(value, prior)
        self.nodes.append(node)
        if self.root is None:
            self.root = node
        else:
            self.root = self.merge(self.root, node)           
                
    def remove(self, key):
        assert self.root is not None
        
        t1, t2 = self.split(self.root, key - 1)
        node, t3 = self.split(t2, 1)
        self.root = self.merge(t1, t3)   
        return node.value
    
    def split(self, t, k):
        if t is None:
            return None, None
        if t.left is None:
            cur = 0
        else:
            cur = t.left.key
        if k > cur:
            t1, t2 = self.split(t.right, k - cur - 1)
            t.right = t1
            t.update_data()
            return t, t2
        else: # k <= t.key
            t1, t2 = self.split(t.left, k)
            t.left = t2
            t.update_data()

            return t1, t
    
    def merge(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        if t1.prior > t2.prior:
            t1.right = self.merge(t1.right, t2)
            t1.update_data()
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            t2.update_data()
            return t2

        

            
    
        
t = Treap()

n, p = read_int_list()
ans = []
for i in range(n):
    t.insert(i + 1, random.randint(1, n))
index = 0
for i in range(n):
    index = (index + p - 1) % len(t)
    res = t.remove(index + 1)
    ans.append(res)

write(*ans)