import sys
def input():
    return sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    tri = [1,1,1,2,2,3,4,5,7,9]
    n = int(input())
    if n <= 10:
        print(tri[n-1])
    else:
        for i in range(10, n):
            tri.append(tri[i-1] + tri[i-5])
        print(tri[-1])