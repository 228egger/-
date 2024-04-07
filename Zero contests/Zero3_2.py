import sys
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
    def __init__(self, key, prior):
        self.key = key
        self.prior = prior
        self._left = None
        self._right = None
        self._parent = None
        
    # T.left = T_1
    
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
            
    def insert(self, key, prior):
        node = self.node_class(key, prior)
        self.nodes.append(node)
        if self.root is None:
            self.root = node
        else:
            self.root = self._insert(self.root, node)
            
    def _insert(self, t, node: TreapNode):
        t1, t2 = self.split(t, node.key)
        t1 = self.merge(t1, node)
        return self.merge(t1, t2)


                
    def split(self, t, k):
        if t is None:
            return None, None
        if k > t.key:
            t1, t2 = self.split(t.right, k)
            t.right = t1
            return t, t2
        else: # k <= t.key
            t1, t2 = self.split(t.left, k)
            t.left = t2
            return t1, t
    
    def merge(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        if t1.prior > t2.prior:
            t1.right = self.merge(t1.right, t2)
            return t1
        else:
            t2.left = self.merge(t1, t2.left)
            return t2

    def _upper_bound(self, t, node):
        t1, t2 = self.split(t, node.key)
        if t2 is not None:
            tmp = t2
            while tmp._left is not None and tmp._left.key >= node.key:
                tmp = tmp._left
            t = self.merge(t1, t2)
            return tmp.key, t
        return -1, t
       
class TreapNodeIndex(TreapNode):
    def __init__(self, key, val, idx):
        super().__init__(key, val)
        self.idx = idx        

class TreapIndex(Treap):
    def __init__(self, key=None, prior=None, idx=None, node_class=TreapNodeIndex):
        self.nodes = []
        self.node_class = node_class
        if key is None:
            assert prior is None
            assert idx is None
            self.root = None
        else:
            self.root = node_class(key, prior, idx)
            self.nodes.append(self.root)
    
    def insert(self, key, prior, idx):
        node = self.node_class(key, prior, idx)
        self.nodes.append(node)
        if self.root is None:
            self.root = node
        else:
            self.root = self._insert(self.root, node)
    
    def upper_bound(self, key, prior, idx):
        node = self.node_class(key, prior, idx)
        if self.root is None:
            return -1
        else:
            num, self.root = self._upper_bound(self.root, node)
            return num



n = read_int()
t = TreapIndex()
last_arg = None
prev_num = None
for idx in range(n):
    curr_arg, num = input().split()
    num = int(num)
    curr_arg = str(curr_arg)
    if curr_arg == '+':
        if last_arg != '?':
            if t.upper_bound(num, idx, -1) != num:
                t.insert(num, idx, idx)
                last_arg = curr_arg
        else:
            if t.upper_bound((num + prev_num) % 10 ** 9, idx, -1) != num:
                t.insert((num + prev_num) % 10 ** 9, idx, idx)
                last_arg = curr_arg
    elif curr_arg == '?':
        prev_num = t.upper_bound(num, idx, -1)
        last_arg = '?'
        print(prev_num)
