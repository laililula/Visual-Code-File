import sys

def Hash(charL):
    MOD = 1234567891
    total = 0
    power = 1
    for i in range(len(charL)):
        ch = ord(charL[i]) - ord('a') + 1
        total = (total + ch*power) % MOD
        power *= 31
    print(total)

L = int(input())
charL = list(sys.stdin.readline().rstrip())
Hash(charL)