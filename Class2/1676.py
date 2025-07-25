def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fact(n-1)
    
N = int(input())
cnt = 0
for i in reversed(str(fact(N)).strip()):
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)