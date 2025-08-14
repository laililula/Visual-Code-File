import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

lo, hi = 1, max(lan)
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = sum(x // mid for x in lan)

    if cnt >= n:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
