import sys
a = sys.stdin.readline().rstrip()
result = ''.join([ch.upper() if ch.islower() else ch.lower() for ch in a])
print(result)