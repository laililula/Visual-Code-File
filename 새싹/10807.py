import sys

a = int(input())
list = list(map(int, sys.stdin.readline().split()))
b = int(input())
print(list.count((b)))