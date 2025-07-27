import sys
def input():
    return sys.stdin.readline().rstrip()
while True:
    flag = True
    stack = []
    line = input()
    if line == ".":
        break
    for ch in line:
        if ch == ".":
            break
        if ch == "(" or ch == "[":
            stack.append(ch)
        elif ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif ch == "]":
            if stack and stack[-1] == "[":
                    stack.pop()
            else:
                flag = False
                break
    if not stack and flag:
        print("yes")
    else:
        print("no")