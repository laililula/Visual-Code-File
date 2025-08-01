import sys
def input():
    return sys.stdin.readline().rstrip()
N, M = map(int, input().split())
pcdict = dict()
for n in range(N):
    pcdict[n+1] = input()
pcdict_R ={v:k for k,v in pcdict.items()}
for _ in range(M):
    m = input()
    if m.isdigit():
        print(pcdict[int(m)])
    else:
        print(pcdict_R[m])