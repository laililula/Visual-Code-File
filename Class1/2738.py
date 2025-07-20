# import sys
# import numpy as np

# a, b = map(int, input().split())
# matrixA = np.array([list(map(int, sys.stdin.readline().split())) for _ in range(a)])
# matrixB = np.array([list(map(int, sys.stdin.readline().split())) for _ in range(a)])
# for i in matrixA+matrixB:
#     print(*i)

import sys

def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

a, b = map(int, input().split())
matrixA = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
matrixB = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
for i in add_matrix(matrixA, matrixB):
    print(*i)