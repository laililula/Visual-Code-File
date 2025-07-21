T = int(input())
#def floor(k, n):
#    if k == 0:
#        return n
#    elif n == 1:
#        return 1
#    return floor(k-1, n) + floor(k, n-1)
dp = [[0]*15 for _ in range(15)]

for i in range(15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])
    #if k == 0:
    #    print(n)
    #else:
    #    print(floor(k, n))
        