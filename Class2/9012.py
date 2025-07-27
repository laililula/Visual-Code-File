import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
for _ in range(N):
    flag = True
    stack = []
    for ch in input().strip():
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
    if not stack and flag:
        print("YES")
    else:
        print("NO")