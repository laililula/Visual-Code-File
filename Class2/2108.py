import sys
import math
def roundup(n):
    return math.floor(n+0.5)
def input():
    return sys.stdin.readline()
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
num.sort()
print(roundup(sum(num)/len(num)))
print(num[len(num)//2])
numdict = {}
for i in num:
    numdict[i] = numdict.get(i, 0) + 1
maxvalue = max(numdict.values())
maxkeys = sorted([k for k, v in numdict.items() if v == maxvalue])
print(maxkeys[1]) if len(maxkeys) >= 2 else print(maxkeys[0])
print(max(num)-min(num))