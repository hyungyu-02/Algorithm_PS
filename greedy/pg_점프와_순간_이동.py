# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 1

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            ans += 1
            n //= 2

    return ans

# 더 깔끔한 풀이
"""

def solution(n):
    ans = 0
    while n > 0:
        ans += n % 2
        n //= 2
    return ans

# ======================= OR

def solution(n):
    return bin(n).count('1')

# 10진수 -> 2진수 변환 과정이 2로 나눠 나가는 과정에서 나머지가 1일 때 1을 적는 것이
# 이 문제 풀이에서 나머지가 1인 순간 1을 더하는 것과 수학적으로 일치함
"""
