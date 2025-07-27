import sys
def input():
    return sys.stdin.readline()
N = int(input())
nList = list(map(int, input().split()))
cardDict = {}
for i in nList:
    cardDict[i] = cardDict.get(i, 0) + 1
M = int(input())
mList = list(map(int, input().split()))
[print(' '.join(str(cardDict.get(i, 0)) for i in mList))]