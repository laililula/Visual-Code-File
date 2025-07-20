import sys
for _ in range(int(input())):
    cnt = 1
    total_sum = 0
    for i in list(sys.stdin.readline().rstrip()):
        if i == 'O':
            total_sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(total_sum)