import sys
for _ in range(int(input())):
    ch = sys.stdin.readline().rstrip()
    print(ch[0]+ch[-1])