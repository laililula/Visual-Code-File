import math
import sys
def input():
    return sys.stdin.readline()
def round(x):
    return math.floor(x + 0.5)
N = int(input())
if N == 0:
    print(0)
    exit()
score = []
total = 0
exc = round(N * 0.15)
for _ in range(N):
    score.append(int(input()))
score.sort()
print(round(sum(score[exc:N-exc]) / (N-exc*2)))