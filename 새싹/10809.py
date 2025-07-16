import sys
S = list(sys.stdin.readline().rstrip())
Alpha_dict = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}
for i in Alpha_dict.keys():
    if i in S:
        Alpha_dict[i] = S.index(i)
x = ' '.join([str(i) for i in Alpha_dict.values()])
print(x)