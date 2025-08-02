import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
dp = [1, 3, 5]
sumdp = [1, 4, 9]
for i in range(3, n):
    if i % 2 == 1:
        dp.append((sumdp[i-1] + 2) % 10007)
    else:
        dp.append((sumdp[i-1] + 1) % 10007)
    sumdp.append(dp[i]+sumdp[i-1])
print(dp[n-1])