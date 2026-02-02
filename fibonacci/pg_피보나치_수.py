# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0

    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)

    for i in range(2, n + 1):
        fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % 1234567)
        # (A + B) % M = ((A % M) + (B % M)) % M

    return fibonacci[n]
