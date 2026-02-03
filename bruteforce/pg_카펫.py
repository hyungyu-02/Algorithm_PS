# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):

    total = brown + yellow

    for h in range(3, int(total**0.5) + 1):
        if total % h == 0:
            w = total // h
            if (h-2) * (w-2) == yellow:
                return [w, h]
