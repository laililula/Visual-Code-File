import sys
#from collections import deque
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()
#def bfs(x, y):    =====웬만하면 bfs 큐=====
#    queue = deque()
#    queue.append((x, y))
#    cmap[x][y] = 0
#    while queue:
#      cx, cy = queue.popleft()
#        for i in range(4):
#            nx = cx + dx[i]
#            ny = cy + dy[i]
#            if 0 <= nx < n and 0 <= ny < m and cmap[nx][ny] == 1:
#                cmap[nx][ny] = 0
#                queue.append((nx, ny))
#def dfs(x, y):     =====웬만하면 dfs 스택=====
#    stack = [(x, y)]
#    while stack:
#        cx, cy = stack.pop()
#        if 0 <= cx < n and 0 <= cy < m and cmap[cx][cy] == 1:
#            cmap[cx][cy] = 0
#            for i in range(4):
#                nx = cx + dx[i]
#                ny = cy + dy[i]
#                stack.append((nx, ny))
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if cmap[x][y] == 1:
        cmap[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    cmap = [[0] * m for _ in range(n)]
    for _ in range(k):
        j, i = map(int, input().split())
        cmap[i][j] = 1
    for x in range(n):
        for y in range(m):
            if cmap[x][y] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)