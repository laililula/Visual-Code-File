import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
atmList = list(map(int, input().split()))
atmList.sort()
sumPart = 0
sumTotal = 0
for i in range(len(atmList)):
    sumPart += atmList[i]
    sumTotal += sumPart
print(sumTotal)