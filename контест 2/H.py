n = int(input())

for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    curr_pos = 0
    count = 0
    num_of_previous = 0
    res = {}
    for i in range(len(a)):
        res[a[i] - i] = res.get(a[i] - i, 0) + 1
    for i in res:
        count += res[i] * (res[i] - 1) / 2
    print(int(count))