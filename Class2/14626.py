import sys
def input():
    return sys.stdin.readline()

ISBN = list(map(str, input().strip()))
total = 0
for i in range(13):
    if ISBN[i] == '*':
        num = i
        continue
    else:
        if i % 2 == 0:
            total += int(ISBN[i])
        else:
            total += int(ISBN[i]) * 3
for i in range(10):
    if num % 2 == 0:
        resTotal = total + i
    else:
        resTotal = total + i*3
    if resTotal % 10 == 0:
        print(i)
        break