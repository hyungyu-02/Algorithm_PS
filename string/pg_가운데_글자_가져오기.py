# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2 - 1: len(s)//2 + 1]
    else:
        return s[len(s)//2]
