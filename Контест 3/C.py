class SegTreeNode:  
    def __init__(self, idx, max = 0, sum = 0):
        self.idx = idx # index in a
        self.max = max
        self.sum = sum
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
            self.a[fst+i] = SegTreeNode(fst+i, 0, 0)
            self.a[fst+i].leftmost = i
            self.a[fst+i].rightmost = i
            
        for i in range(fst+n, self.total_length):
            self.a[i] = SegTreeNode(i, 0, 0)
            self.a[i].leftmost = i
            self.a[i].rightmost = i
            
        for i in range(fst-1, -1, -1):
            left = self.a[self.left(i)]
            right = self.a[self.right(i)]
            self.a[i] = SegTreeNode(i, 0, 0)
            self.a[i].leftmost = left.leftmost
            self.a[i].rightmost = right.rightmost

    def __call__(self, l, r, idx = 0): # l и r нумеруются с нуля как массив inp у нас в памяти      
        if idx >= len(self.a):
            return 0
        if self.a[idx].leftmost > r or self.a[idx].rightmost < l:
            return 0
        if (l <= self.a[idx].leftmost and self.a[idx].rightmost <= r):
            return self.a[idx].max
        return max(self(l, r, self.left(idx)), self(l, r, self.right(idx))) + self.a[idx]
    
    def update(self, l, r, sum, idx = 0):
        if idx >= len(self.a):
            return
        if l <= self.a[idx].leftmost and self.a[idx].rightmost <= r:
            self.a[idx].max += sum
            self.a[idx].sum += sum
            return
        if self.a[idx].leftmost > r or self.a[idx].rightmost < l:
            return
        self.update(l, r, sum, self.left(idx))
        self.update(l, r, sum, self.right(idx))
        self.a[idx].max = max(self.a[self.left(idx)].max, self.a[self.right(idx)].max) + self.a[idx].sum




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
rmq = SegTree([0 for _ in range(n)])
for _ in range(k):    
    arg = input().split()
    if arg[0] == 'build':
        l, r, val = map(int, arg[1:])
        l, r, = l-1, r-1
        rmq.update(l, r, val, 0)
    else:
        l, r = map(int, arg[1:])
        l, r, = l-1, r-1
        print(rmq(l, r))