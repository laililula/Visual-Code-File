import sys

def input():
    return sys.stdin.readline()

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(input())] += 1

for i in range(1, 10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)