#Math, Prime Number, 에라토스테네스의 체
prime_num = [2, 3]
for i in range(5, 9998):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        prime_num.append(i)

t = int(input())
for _ in range(t):
    n = int(input())
    small = n//2
    while True:
        if small in prime_num:
            break
        small -= 1
    pnt = prime_num.index(small)
    while True:
        if (n-prime_num[pnt]) in prime_num:
            print(prime_num[pnt], n-prime_num[pnt])
            break
        else:
            pnt -= 1
