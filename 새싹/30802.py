import sys
import math
N = int(input())
Tlist = list(map(int, sys.stdin.readline().rstrip().split()))
TPlist = list(map(int, sys.stdin.readline().rstrip().split()))
print(math.ceil(Tlist[0]/TPlist[0]) + math.ceil(Tlist[1]/TPlist[0]) + math.ceil(Tlist[2]/TPlist[0]) + math.ceil(Tlist[3]/TPlist[0]) + math.ceil(Tlist[4]/TPlist[0]) + math.ceil(Tlist[5]/TPlist[0]))
print(f"{math.floor(N/TPlist[1])} {N%TPlist[1]}")