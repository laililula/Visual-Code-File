import sys
n = int(input())
list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
print(f"{list[0]} {list[-1]}")