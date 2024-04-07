import sys
input = sys.stdin.buffer.readline

def read_int():
    return int(input())

n = read_int()
max_15, max_3, max_5, max_1 = -float('inf'), -float('inf'), -float('inf'), -float('inf')
max_15_2 = -float('inf')
for _ in range(n):
    tmp = read_int()
    if not(tmp % 3) and (tmp % 5):
        max_3 = max(max_3, tmp)
    elif not(tmp % 5) and (tmp % 3):
        max_5 = max(max_5, tmp)
    elif not(tmp % 15):
        max_15_2 = min(max_15, tmp)
        max_15 = max(max_15, tmp)
    if (tmp % 15):
        max_1 = max(max_1, tmp)

max_ = -float('inf')
res = [max_3 * max_5, max_15 * max_15_2, max_15 * max_1]
for i in res:
    if i < float('inf'):
        max_ = max(max_, i)
print(max_)
sys.stdout.flush()