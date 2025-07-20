totalM = 1440
h, m = map(int, input().split())
sumM = h*60 + m
if sumM - 45 < 0:
    alarm = 1440 - abs(sumM - 45)
else:
    alarm = sumM - 45
h = alarm // 60
m = alarm % (h*60) if h != 0 else alarm
print(f"{h} {m}")