import sys
def input():
    return sys.stdin.readline().rstrip()
N, M = map(int, input().split())
noset = set()
res = list()
cnt = 0
for _ in range(N):
    noset.add(input())
for _ in range(M):
    m = input()
    if m in noset:
        cnt += 1
        res.append(m)
print(cnt)
print('\n'.join(map(str, sorted(res))))