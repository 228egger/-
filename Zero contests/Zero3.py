n = int(input())

swap = dict()
for _ in range(n):
    a1, a2 = map(int, input().split())
    if a1 in swap:
        if a2 in swap:
            print(abs(swap[a1] - swap[a2]))
            swap[a1], swap[a2] = swap[a2], swap[a1]
        else:
            print(abs(swap[a1] - a2))
            swap[a2] = swap[a1]
            swap[a1] = a2
    elif a2 in swap:
        if a1 in swap:
            print(abs(swap[a1] - swap[a2]))
            swap[a2], swap[a1] = swap[a1], swap[a2]
        else:
            print(abs(swap[a2] - a1))
            swap[a1] = swap[a2]
            swap[a2] = a1
    else:
        print(abs(a1 - a2))
        swap[a2] = a1
        swap[a1] = a2
