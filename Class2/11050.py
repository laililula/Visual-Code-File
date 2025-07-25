n, k = map(int, input().split())
total = 1
for _ in range(k):
    total *= n
    n -= 1
for _ in range(k):
    total //= k
    k -= 1
print(total)