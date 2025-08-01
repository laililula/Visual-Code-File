import sys
def input():
    return sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    total = 1
    cloths = dict()
    for _ in range(n):
        v, k = input().split()
        cloths[k] = cloths.get(k, 0) + 1
    for c in cloths.keys():
        total *= (cloths[c]+1)
    print(total-1)