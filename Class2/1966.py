from collections import deque
import sys
def input():
    return sys.stdin.readline()
N = int(input())
for _ in range(N):
    queue = deque()
    cnt = 0
    a, pos = map(int, input().split())
    queue.extend(list(map(int, input().split())))
    while True:
        if queue[0] != max(queue):
            down = queue.popleft()
            queue.append(down)
            pos = (pos-1) % a
        else:
            queue.popleft()
            cnt += 1
            a -= 1
            if pos == 0:
                print(cnt)
                break
            else:
                pos = (pos-1) % a