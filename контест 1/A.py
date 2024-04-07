import sys
input = sys.stdin.buffer.readline

def read_int():
    return int(input())


left_1, left_2, right_1, right_2 = float('inf'), float('inf'), -float('inf'), -float('inf')
high_right, high_left = -float('inf'), -float('inf')
n = read_int()
for _ in range(n):
    x, y = map(float, input().split())


    if (abs(y) > 0 and x > 0):
        high_right = max(high_right, abs(y))
    elif (abs(y) > 0 and x < 0):
        high_left = max(high_left, abs(y))
    if (y == 0) and (x > 0):
        if (x < left_1):
            if (abs(left_1) != float('inf')):
                right_1 = max(right_1, left_1)
            left_1 = x
        elif (x > right_1):
            if (abs(right_1) != float('inf')):
                left_1 = min(right_1, left_1)
            right_1 = x
    elif (y == 0) and (x < 0):
        if (x > right_2):
            if (abs(right_2) != float('inf')):
                left_2 = min(right_2, left_2)
            right_2 = x
        elif (x < left_2):
            if (abs(left_2) != float('inf')):
                right_2 = max(right_2, left_2)
            left_2 = x
s_1 = abs((right_1 - left_1) * high_right / 2)
s_2 = abs((left_2 - right_2) * high_left / 2)
if min(s_1, s_2) == float('inf'):
    print(0)
else:
    if max(s_1, s_2) == float('inf'):
        print(min(s_1, s_2))
    else:
        print(max(s_1, s_2))

sys.stdout.flush()
