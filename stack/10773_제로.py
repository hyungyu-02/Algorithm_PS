#스택
import sys

k = int(input())

lst = []
total = 0

for _ in range(k):
    lst.append(int(sys.stdin.readline()))
    
jump = 0
for i in range(len(lst)-1, -1, -1):
    if lst[i] == 0:
        jump += 1
    else:
        if jump > 0:
            jump -= 1
        else:
            total += lst[i]
print(total)
