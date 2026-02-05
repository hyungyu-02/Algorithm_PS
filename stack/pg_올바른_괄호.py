# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    count = 0

    for bracket in s:
        if bracket == '(':
            count += 1
        else:
            if not count:
                return False
            else:
                count -= 1

    return not count
