import math
n, m = map(int, input().split())
for i in range(n, m+1):
    flag = True
    if i == 0 or i == 1:
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)