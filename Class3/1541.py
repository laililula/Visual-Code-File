import sys
import re
def input():
    return sys.stdin.readline().rstrip()
s = input()
exp = re.split(r'([-+])', s)
total = int(exp[0])
cnt = 0
cnt1 = 0
for i, token in enumerate(exp):
    idx = 2
    if cnt1 != cnt*2+1:
        cnt1 += 1
        continue
    if token == '-':
        while i+idx < len(exp) and exp[i+idx] == '+':
            total -= int(exp[i+idx-1])
            idx += 2
            cnt += 1
        total -= int(exp[i+idx-1])
    elif token == '+':
        total += int(exp[i+1])
print(total)