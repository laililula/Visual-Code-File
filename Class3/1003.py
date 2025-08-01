import sys
def input():
    return sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n = int(input())
    fibonacciList = [[1, 0], [0, 1]]
    i = 0
    if (n == 0):
        print(' '.join(map(str, fibonacciList[0])))
        continue
    elif (n == 1):
        print(' '.join(map(str, fibonacciList[1])))
        continue
    else:
        while True:
            row = []
            row = [fibonacciList[i][j] + fibonacciList[i+1][j] for j in range(2)]
            fibonacciList.append(row)
            if i == n-2:
                break
            i += 1
    print(' '.join(map(str, fibonacciList[-1])))