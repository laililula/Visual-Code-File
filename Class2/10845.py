import sys
def input():
    return sys.stdin.readline()
N = int(input())
queue = []
f, r = 0, -1
for _ in range(N):
    command = input().split()

    if command[0] == "push":
        queue.append(command[1])
        r += 1
    elif command[0] == "size": print(r-f+1)
    elif command[0] == "pop":
        if queue:
            print(queue[f])
            f += 1
            if f == len(queue):
                queue = []
                f, r = 0, -1
        else:
            print(-1)
    elif command[0] == "empty": print(0) if queue else print(1)
    elif command[0] == "front":
        if queue:
            print(queue[f])
        else:
            print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[r])
        else:
            print(-1)