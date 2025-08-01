import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1, 2, 4]
    while len(dp) < n:
        dp.append(dp[-1] + dp[-2] + dp[-3])
    print(dp[n - 1])