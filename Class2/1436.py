N = int(input())
cnt = 1
start = 666
while True:
    if cnt == N:
        print(start)
        break
    start += 1
    if "666" in str(str(start)):
        cnt += 1