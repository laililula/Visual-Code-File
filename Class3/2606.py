import sys
def input():
    return sys.stdin.readline().rstrip()
cpt = int(input())
net = {1}
net1 = []
for _ in range(int(input())):
    net1.append(set(map(int, input().split())))
update = True
while update:
    update = False
    for net2 in net1:
        if any(c in net for c in net2):
            if not net2.issubset(net):
                net.update(net2)
                update = True
print(len(net)-1)