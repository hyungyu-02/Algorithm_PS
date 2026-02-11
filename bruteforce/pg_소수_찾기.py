# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import math

def solution(numbers):
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    
    visited = [False] * len(numbers)
    found_prime = set()
    
    def dfs(number):
        if number:
            num = int(number)
            if num not in found_prime:
                if is_prime(num):
                    found_prime.add(num)
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(number + numbers[i])
                visited[i] = False
    
    dfs("")
    
    return len(found_prime)

# permutations(조합)를 이용한 풀이
"""
from itertools import permutations
import math

def solution(numbers):
    all_numbers = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            all_numbers.add(int("".join(p)))
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True
    
    return len([n for n in all_numbers if is_prime(n)])
"""
