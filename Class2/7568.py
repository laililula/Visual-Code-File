import sys
def input():
    return sys.stdin.readline()

N = int(input())
blist = []
res = []
for i in range(N):
    blist.append(list(map(int, input().split())))
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if blist[i][0] < blist[j][0] and blist[i][1] < blist[j][1]:
            cnt += 1
    res.append(cnt + 1)
print(' '.join(map(str, res)))