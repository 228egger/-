import math

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def gen_c(a, b, x, y):
    return a * x + b * y
a, b, c = map(int, input().split())
x_prev, y_prev = math.copysign(1, a), 0
c_prev = gen_c(a, b, x_prev, y_prev)
x_cur, y_cur = 0, math.copysign(1, b) 
c_cur = gen_c(a, b, x_cur, y_cur)
if c_cur > c_prev:
    x_tmp, y_tmp, c_tmp = x_cur, y_cur, c_cur
    x_cur, y_cur, c_cur = x_prev, y_prev, c_prev
    x_prev, y_prev, c_prev = x_tmp, y_tmp, c_tmp
d = gcd(abs(a), abs(b))
x_0, y_0 = 0, 0
if (c % d):
    print("No")
else:
    if (c == c_prev):
        x_0, y_0 = math.copysign(1, a), 0
    elif (c == c_cur):
        x_0, y_0 = 0, math.copysign(1, b)
    else:
        while (d != c_cur):
            delim = c_prev // c_cur
            x_tmp, y_tmp, c_tmp = x_cur, y_cur, c_cur
            x_cur = x_prev - x_cur * delim
            y_cur = y_prev - y_cur * delim
            c_cur = c_prev - c_cur * delim
            x_prev, y_prev, c_prev = x_tmp, y_tmp, c_tmp

        mult = c // d
        x_0, y_0 = mult * x_cur, mult * y_cur
    if x_0 <= 0:
        while x_0 <= 0:
            if b < 0:
                x_0 -= b / d
                y_0 += a/d
            elif b > 0:
                x_0 += b / d
                y_0 -= a/d
            else:
                break
    elif x_0 > 0:
        while x_0 > 0:
            if b < 0:
                x_0 += b / d
                y_0 -= a / d
            elif b > 0:
                x_0 -= b / d
                y_0 += a / d
            else:
                break
        if b < 0:
            x_0 -= b / d
            y_0 += a / d
        else:
            x_0 += b / d
            y_0 -= a / d
    print(int(x_0), int(y_0))



