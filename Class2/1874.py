import sys
def input():
    return sys.stdin.readline()
n = int(input())
num = []
nlist = []
res = []
prev = 1
for _ in range(n):
    num.append(int(input()))
cnt = 0
for i in num:
    if prev <= i:
        for j in range(cnt+1, i+1):
            nlist.append(j)
            res.append('+')
            cnt += 1
    if nlist[-1] == i:
        nlist.pop()
        res.append('-')
    else:
        print("NO")
        exit()
    prev = i
print('\n'.join(list(map(str, res))))