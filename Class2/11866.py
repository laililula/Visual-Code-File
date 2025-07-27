n, k = map(int, input().split())
cnt = 0
idx = 0
cir = list(range(1, n+1))
cirT = [True] * n
res = []
while True:
    idx = idx % n
    if cirT[idx] == True:
        cnt += 1
        if cnt == k:
            res.append(cir[idx])
            cirT[idx] = False
            cnt = 0
    idx += 1
    if len(res) == n:
        break
print("<"+ ', '.join(map(str, res)) +">")