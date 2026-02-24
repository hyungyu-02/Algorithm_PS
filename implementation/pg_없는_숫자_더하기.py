# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = 45
    for number in numbers:
        answer -= number
    return answer
