# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    isInit = True
    for ch in s:
        ch = ch.lower()
        if isInit:
            ch = ch.upper()
            isInit = False
        answer += ch
        if ch == ' ':
            isInit = True
    return answer
