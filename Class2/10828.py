import sys
def input():
    return sys.stdin.readline()
def push(stack, n):
    stack.append(n)
def size(stack):
    print(len(stack))
def pop(stack):
    if stack:
        print(stack[len(stack)-1])
        stack.pop()
    else:
        print(-1)
def empty(stack):
    print(0) if stack else print(1)
def top(stack):
    print(stack[len(stack)-1]) if stack else print(-1)
N = int(input())
stack = []
for _ in range(N):
    command = input().split()

    if command[0] == "push": push(stack, int(command[1]))
    elif command[0] == "size": size(stack)
    elif command[0] == "pop": pop(stack)
    elif command[0] == "empty": empty(stack)
    elif command[0] == "top": top(stack)