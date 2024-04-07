class SegTreeNode:  
    def __init__(self, idx, val=0, count = 1):
        self.idx = idx # index in a
        self.val = val
        self.count = count
        self.leftmost = None
        self.rightmost = None
        
    def __str__(self):
        return f"(idx={self.idx}, val={self.val})"

    def __repr__(self):
        return f"(idx={self.idx}, val={self.val})"
    

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
        
        for i, val in enumerate(inp):
            self.a[fst+i] = SegTreeNode(fst+i, -1, count = 1)
            self.a[fst+i].leftmost = i
            self.a[fst+i].rightmost = i
            
        for i in range(fst+n, self.total_length):
            self.a[i] = SegTreeNode(i, -1, 0)
            self.a[i].leftmost = i
            self.a[i].rightmost = i
            
        for i in range(fst-1, -1, -1):
            left = self.a[self.left(i)]
            right = self.a[self.right(i)]
            total_count = left.count + right.count
            self.a[i] = SegTreeNode(i, -1, count = total_count)
            self.a[i].leftmost = left.leftmost
            self.a[i].rightmost = right.rightmost
            
                    
    
    def __call__(self, l, r, idx = 0): # l и r нумеруются с нуля как массив inp у нас в памяти 
        if idx >= len(self.a):
            return 0
        if self.a[idx].leftmost > r or self.a[idx].rightmost < l:
            return 0
        if self.a[idx].val >= 0 and (l <= self.a[idx].leftmost and self.a[idx].rightmost <= r):
            return self.a[idx].val * self.a[idx].count
        if self.a[idx].leftmost == self.a[idx].rightmost and self.a[idx].val == -1:
            return 0
        if self.a[idx].val >= 0:
            self.a[self.left(idx)].val = self.a[idx].val
            self.a[self.right(idx)].val = self.a[idx].val
            self.a[idx].val = -1
        return self(l, r, self.left(idx)) + self(l, r, self.right(idx))
            
    def update(self, l, r, val, idx):
        if idx >= len(self.a):
            return
        if l <= self.a[idx].leftmost and self.a[idx].rightmost <= r:
            self.a[idx].val = val
            return
        if self.a[idx].leftmost > r or self.a[idx].rightmost < l:
            return
        if self.a[idx].val < 0:
            self.update(l, r, val, self.left(idx))
            self.update(l, r, val, self.right(idx))
        elif self.a[idx].val >= 0:
            self.a[self.left(idx)].val = self.a[idx].val
            self.a[self.right(idx)].val = self.a[idx].val
            self.a[idx].val = -1
            self.update(l, r, val, self.left(idx))
            self.update(l, r, val, self.right(idx))


    def parent(self, idx): # Если нумерация с единицы: parent(idx) = idx // 2
        p = (idx + 1) // 2 - 1
        return p if p >= 0 else None
        
    def left(self, idx):
        c = (idx + 1) * 2 - 1
        return c if c < len(self.a) else None
    
    def right(self, idx):
        c = (idx + 1) * 2 
        return c if c < len(self.a) else None



n, k = map(int, input().split())
rmq = SegTree([-1 for _ in range(n)])
for _ in range(k):    
    arg = input().split()
    if arg[0] == 'A':
        l, r, val = map(int, arg[1:])
        l, r, = l-1, r-1
        rmq.update(l, r, val, 0)
    else:
        l, r = map(int, arg[1:])
        l, r, = l-1, r-1
        print(rmq(l, r))
