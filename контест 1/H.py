import sys
input = sys.stdin.buffer.readline



s = input().rstrip()
t = input().rstrip()


pivot = -float('inf')
cur_el = len(t) - 1
for j in range(len(s) - 1, -1, -1):
    if t[cur_el] == s[j]:
        cur_el -= 1
    if cur_el == -1:
        pivot = j
        break

for i in range(len(s)):
    if i > pivot:
        print("no")
    else:
        print("yes")