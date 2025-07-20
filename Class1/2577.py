import sys
x = 1
for _ in range(3):
    x *= int(input())
char_dict = {i: 0 for i in range(10)}
for char in str(x):
    if int(char) in char_dict:
        char_dict[int(char)] += 1
[print(char_dict[i]) for i in range(10)]