def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def find_sol(a, b, c):
    if b == 0:
        return (True, c / a, 0)
    d = gcd(a, b)
    if c % d:
        return (False, -1, -1)
    a_ = a % b
    flag, x_0, y_0 =  find_sol(b, a_, c)
    return (flag, y_0, x_0 - a // b * y_0)




a, b, c = map(int, input().split())
d = gcd(abs(a), abs(b))
flag, x_0, y_0 = find_sol(abs(a), abs(b), c)
if a < 0:
    x_0 *= -1
if b < 0:
    y_0 *= -1
if flag:
    if x_0 <= 0:
        while x_0 <= 0:
            if b < 0:
                x_0 -= b / d
                y_0 += a/d
            else:
                x_0 += b / d
                y_0 -= a/d
    elif x_0 > 0:
        while x_0 > 0:
            if b < 0:
                x_0 += b / d
                y_0 -= a / d
            if b > 0:
                x_0 -= b / d
                y_0 += a / d
        if b < 0:
            x_0 -= b / d
            y_0 += a / d
        else:
            x_0 += b / d
            y_0 -= a / d
    print(int(x_0), int(y_0))
else:
    print("No")



