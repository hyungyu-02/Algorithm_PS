# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    answer = 0

    steps = [1, 1]

    if n == 1:
        return steps[n]

    for i in range(2, n+1):
        steps.append((steps[i-1] + steps[i-2]) % 1234567)

    return steps[n]

# n번째 단계에 도달하는 방법은 n-1번째 단계에서 1칸 뛰는 방법 + n-2번째 단계에서 2칸 뛰는 방법
