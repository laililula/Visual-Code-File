import sys
print(sum(x**2 for x in map(int, sys.stdin.readline().split())) % 10)