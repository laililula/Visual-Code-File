N = int(input())
maxb = 1
cnt = 1
while maxb < N:
    maxb += 6*cnt
    cnt += 1
print(cnt)