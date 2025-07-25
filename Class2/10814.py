import sys
def input():
    return sys.stdin.readline()

N = int(input())
joinList = []
for i in range(N):
    joinList.append(list(map(str, input().split())))
for i in sorted(joinList, key=lambda x: int(x[0])):
    print(' '.join(map(str, i)))