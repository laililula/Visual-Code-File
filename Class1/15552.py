import sys

a= int(input())
for _ in range(a):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)