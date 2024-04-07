import sys
input = sys.stdin.buffer.readline

def read_int():
    return int(input())
n = read_int()
l = 1
r = n
cur = (l + r) // 2 + (l + r) % 2
ans = 0
while ans != 1:
    print(cur)
    sys.stdout.flush()
    ans = read_int()
    tmp = cur
    if ans == 2:
        l = cur
        cur = (l + r) // 2 + (l + r) % 2
    elif ans == 0:
        r = cur
        cur = (l + r ) // 2
    else:
        break
