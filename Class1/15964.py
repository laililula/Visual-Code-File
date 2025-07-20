import sys

def cal(a, b):
    return (a+b)*(a-b)

print(cal(*map(int, sys.stdin.readline().rstrip().split())))