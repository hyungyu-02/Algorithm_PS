# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x + (x*i))
    return answer
