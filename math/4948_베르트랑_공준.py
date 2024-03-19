#Math, Prime Number, 에라토스테네스의 체
import sys
input = sys.stdin.readline

N = 123456*2 + 1
prime_num = [0] * N
prime_num[2] = 1
prime_num[3] = 1
for i in range(4, N):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        prime_num[i] = 1


while True:
    n = int(input())
    if n == 0:
        break
    num = 0
    for i in range(n+1, 2*n+1):
        num += prime_num[i]
    print(num)
