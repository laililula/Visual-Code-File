import sys
def input():
    return sys.stdin.readline().rstrip()
N, M = map(int, input().split())
siteDict = dict()
for _ in range(N):
    k, v = map(str, input().split())
    siteDict[k] = v
for m in range(M):
    print(siteDict[input()])