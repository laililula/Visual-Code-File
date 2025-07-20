import sys
list = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
print(max(list))
print(list.index(max(list))+1)