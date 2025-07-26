import math
def power2(n):
    if n <= 0:
        return False
    if n & (n-1) != 0:
        return False
    return True

N = int(input())
if N == 1:
    print(1)
elif power2(N):
    print(N)
else:
    low = pow(2, int(math.log2(N)))
    up = low*2
    mid = (low+up)//2
    if N < mid:
        print(low - abs(N - mid)*2)
    elif N > mid:
        print(low + (N - mid)*2)
    else:
        print(low)