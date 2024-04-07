#!/usr/bin/env python3
import sys
input = sys.stdin.buffer.readline
import bisect



def read_int():
    return int(input())       


n = read_int()
lines = []
bisect.insert(lines, (0, 0))
bisect.insert(lines, (10e6, 10e6))
for i in range(n):
    t = read_int()
    if t > 0:
        upper = bisect.bisect_right((t, 10e6), lines)
        lower = upper - 1
        current = (t, t)
        if (t <= lines[lower][1] + 1):
            t = lines[lower][1] + 1
            new = (lines[lower][0], t)
            lines.pop(lower)
        if (new[1] == lines[upper][0] - 1):
            new[1] = lines[upper][1]
            lines.pop(bisect.bisect_right((t, 10e6), lines))
        
        
    

