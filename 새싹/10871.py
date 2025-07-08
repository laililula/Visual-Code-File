import sys

a, b = map(int, input().split())
list = list(map(int, sys.stdin.readline().split()))
for i in range(a):
    if list[i] < b:
        print(list[i])