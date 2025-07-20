import sys
import math
while True:
    Tlist = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    if Tlist == [0, 0, 0]:
        break
    print("right") if math.sqrt(pow(Tlist[0], 2)+pow(Tlist[1], 2)) == Tlist[2] else print("wrong")