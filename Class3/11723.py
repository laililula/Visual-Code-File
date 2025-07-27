import sys
def input():
    return sys.stdin.readline()
def write(s):
    sys.stdout.write(s)
N = int(input())
sset = set()
for _ in range(N):
    line = list(map(str, input().split()))
    if line[0] == "add": sset.add(int(line[1]))
    elif line[0] == "remove":
        if int(line[1]) in sset:
            sset.remove(int(line[1])) 
    elif line[0] == "check": write("1\n") if int(line[1]) in sset else write("0\n")
    elif line[0] == "toggle": sset.remove(int(line[1])) if int(line[1]) in sset else sset.add(int(line[1]))
    elif line[0] == "all":
        sset = set(map(int, range(1, 21)))
    elif line[0] == "empty": sset.clear()