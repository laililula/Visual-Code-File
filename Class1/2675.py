import sys
for _ in range(int(input())):
    list_z = list(sys.stdin.readline().rstrip().split())
    x = ''.join([i*int(list_z[0]) for i in list_z[1]])
    print(x)