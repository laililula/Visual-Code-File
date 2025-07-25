import sys

N = int(sys.stdin.readline())
nlist = []
for _ in range(N):
    nlist.append(int(sys.stdin.readline()))
print('\n'.join(map(str, sorted(nlist))))