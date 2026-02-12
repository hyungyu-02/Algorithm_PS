# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if s:
            answer += a
        else:
            answer -= a
    return answer
    # 다른 방법
    # return sum(num if sign else -num for num, sign in zip(absolutes, signs))
