a = [int(input()) for _ in range(2)]
if a[0] > 0 and a[1] > 0:
    print(1)
elif a[0] < 0 and a[1] > 0:
    print(2)
elif a[0] < 0 and a[1] < 0:
    print(3)
else:
    print(4)