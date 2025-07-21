import sys
N = int(input())
gradeList = list(map(int, sys.stdin.readline().rstrip().split()))
maxGrade = max(gradeList)
total = 0
for i in range(N):
    total += gradeList[i]/maxGrade*100
print(total/N)