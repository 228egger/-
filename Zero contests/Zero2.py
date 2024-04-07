class Heap:
    def __init__(self):
        self.heap = []
    def Heapify(self, pos):
        while (1):
            left = 2 * pos + 1
            right = 2 * pos + 2
            cur = pos
            if (left < len(self.heap) and (self.heap[cur][1] < self.heap[left][1] or
                (self.heap[cur][1] == self.heap[left][1] and self.heap[cur][2] > self.heap[left][2]))):
                cur = left
            if (right < len(self.heap) and (self.heap[cur][1] < self.heap[right][1] or
                (self.heap[right][1] == self.heap[cur][1] and self.heap[cur][2] > self.heap[right][2]))):
                cur = right
            if cur == pos:
                return pos
            self.heap[pos], self.heap[cur] = self.heap[cur], self.heap[pos]
            pos = cur


    def push(self, value):
        pos = len(self.heap)
        self.heap.append(value)
        parent = (pos - 1) // 2
        while pos > 0 and (self.heap[pos][1] > self.heap[parent][1] or
                           (self.heap[pos][1] == self.heap[parent][1] and self.heap[pos][2] < self.heap[parent][2])):
            self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
            pos = parent
            parent = (pos - 1) // 2

    
    def pop(self):
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.Heapify(0)
        return max

    

n, m = map(int, input().split())
heap = Heap()
s = set()
for i in range(m):
    line = input().split()
    line[1] = int(line[1])
    line.append(i)
    heap.push(line)


for _ in range(m):
    name = heap.pop()
    if name[0] not in s:
        s.add(name[0])
        print(name[0])
