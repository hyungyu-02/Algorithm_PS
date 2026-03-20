# https://school.programmers.co.kr/learn/courses/30/lessons/12953

# 두 자연수 A, B에 대하여, 두 수의 곱은 최대공약수(G)와 최소공배수(L)의 곱과 같다.
# A * B = G * L

import math

def solution(arr):
    def lcm(a, b):
        return (a * b) // math.gcd(a, b)
    
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
        
    return answer


# gcd 직접 구현하는법 (유클리드 호제법)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
