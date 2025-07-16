import sys
import math
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

cnt = 0
N = int(input())
priList = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(N):
    if is_prime(priList[i]) == True:
        cnt += 1
print(cnt)