a = []
while True:
    b = list(map(int, input().split()))
    if b == [0, 0]:
        break
    a.append(b)
for i in range(len(a)):
    print(a[i][0]+a[i][1])