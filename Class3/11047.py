import sys
def input():
    return sys.stdin.readline().rstrip()
N, K = map(int, input().split())
coinList = []
cnt = 0
for _ in range(N):
    coinList.append(int(input()))
for i in range(N-1, -1, -1):
    if K % coinList[i] == 0:
        cnt += K // coinList[i]
        break
    elif K < coinList[i]:
        continue
    else:
        cnt += K // coinList[i]
        K = K % coinList[i]
print(cnt)