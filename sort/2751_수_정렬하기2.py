#sort
import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
#그냥 input()보다 속도가 빠름

num.sort()
#num.sort(reverse = True)

for i in num:
    print(i)
