# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    numbers = list(map(int, s.split()))

    maximum = max(numbers)
    minimum = min(numbers)

    return f"{minimum} {maximum}"
