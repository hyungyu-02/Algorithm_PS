# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def is_prime(num):
        if num <= 1: return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def solution(n, k):
    arr = []
    changed = 0
    i = 1
    while n > 0:
        added = (n % k) * i
        if added == 0:
            if changed > 0:
                arr.append(changed)
                changed = 0
            i = 1
        else:
            changed += added
            i *= 10
        n //= k
    if changed > 0: arr.append(changed)
    
    count = 0
    for a in arr:
        if is_prime(a):
            count += 1
    return count

# string을 이용한 풀이
def is_prime(num):
        if num <= 1: return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def solution(n, k):
    notation_str = ""
    
    while n > 0:
        notation_str = str(n % k) + notation_str
        n //= k
    
    candidate = notation_str.split('0')
    
    count = 0
    for c in candidate:
        if c and is_prime(int(c)):
            count += 1
    
    return count
