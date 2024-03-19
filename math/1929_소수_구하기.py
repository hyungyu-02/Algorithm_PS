#math, prime number, 에라토스테네스의 체
m, n = map(int, input().split())

if m == 1 and n >= 2:
    m = 2
for i in range(m, n+1):
    for num in range(2, int(i**0.5)+1):
        if i % num == 0:
            break
    else:
        print(i)
