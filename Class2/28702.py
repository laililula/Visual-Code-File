cnt = 3
ch = []
for _ in range(3):
    ch.append(input())
for i in range(3):
    if ch[i].isdigit():
        res = int(ch[i])+cnt
        if res % 3 == 0 and res % 5 == 0:
            print("FizzBuzz")
        elif res % 3 == 0 and res %5 != 0:
            print("Fizz")
        elif res % 3 != 0 and res %5 == 0:
            print("Buzz")
        else:
            print(res)
        break
    cnt -= 1