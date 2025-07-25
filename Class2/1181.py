import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
wordMap = [[] for _ in range(51)]
for _ in range(N):
    ch = input()
    wordMap[len(ch)].append(ch)
for i in range(51):
    if not wordMap[i]:
        continue
    else:
        res = list(sorted((set(wordMap[i]))))
        for w in res:
            print(w)