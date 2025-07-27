N = int(input())
stack = []
for _ in range(N):
    m = int(input())
    if m == 0:
        stack.pop()
    else:
        stack.append(m)
print(sum(stack))

#N = int(input())
#total = 0
#stack = []
#pos = -1
#for _ in range(N):
#    m = int(input())
#    if m == 0:
#        total -= stack[pos]
#        stack.pop()
#        pos -= 1
#    else:
#        stack.append(m)
#        total += m
#        pos += 1
#print(total)