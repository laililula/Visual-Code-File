N = int(input())
cnt = 0
r = N % 5
q = N // 5
while True:
    if r % 3 == 0:
        print(q + r // 3)
        break
    else:
        q -= 1
        if q == -1:
            print(-1)
            break
        if (N - q * 5) % 3 == 0:
            print(q + (N - q * 5) // 3)
            break