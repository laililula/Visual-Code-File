i = int(input())
a = [list(map(int, input().split())) for _ in range(i)]
for i in range(i):
    print(a[i][0] + a[i][1])