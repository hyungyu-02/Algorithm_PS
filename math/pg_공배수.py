# https://school.programmers.co.kr/learn/courses/30/lessons/181936

def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0
