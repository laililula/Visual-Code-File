import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def dfs(x: int, y: int, size: int):
    first = board[x][y]
    mono = True
    for i in range(x, x + size):
        if not mono:
            break
        for j in range(y, y + size):
            if board[i][j] != first:
                mono = False
                break
    if mono:
        return (1, 0) if first == 0 else (0, 1)

    half = size // 2
    w1, b1 = dfs(x, y, half)
    w2, b2 = dfs(x, y + half, half)
    w3, b3 = dfs(x + half, y, half)
    w4, b4 = dfs(x + half, y + half, half)
    return (w1 + w2 + w3 + w4, b1 + b2 + b3 + b4)

white, blue = dfs(0, 0, N)
print(white)
print(blue)
