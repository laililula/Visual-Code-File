N, M = map(int, input().split())
chess = [input().strip() for _ in range(N)]

pattern1 = ['WBWBWBWB', 'BWBWBWBW'] * 4
pattern2 = ['BWBWBWBW', 'WBWBWBWB'] * 4

result = 64 

for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = cnt2 = 0
        for x in range(8):
            for y in range(8):
                if chess[i+x][j+y] != pattern1[x][y]:
                    cnt1 += 1
                if chess[i+x][j+y] != pattern2[x][y]:
                    cnt2 += 1
        result = min(result, cnt1, cnt2)

print(result)
