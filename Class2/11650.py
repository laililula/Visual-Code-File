import sys
def input():
    return sys.stdin.readline()

N = int(input())
dotList = []
for _ in range(N):
    dotList.append(list(map(int, input().split())))
slist = sorted(dotList, key=lambda x: (x[0], x[1]))
for i in slist:
    print(*i)