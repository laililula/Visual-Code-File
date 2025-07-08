a = []
full = set(range(1, 31))
for i in range(28):
    a.append(int(input()))
print(sorted(full - set(a))[0])
print(sorted(full - set(a))[1])