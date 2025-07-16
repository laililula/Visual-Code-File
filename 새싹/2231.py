N = int(input())
disList = []
for i in range(max(1, N - (9 * len(str(N)))), N):
    if i + sum(map(int, str(i))) == N:
        disList.append(i)
if not disList:
    print(0)
else:
    print(min(disList))