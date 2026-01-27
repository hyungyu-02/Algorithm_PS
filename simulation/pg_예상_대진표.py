# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    answer = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer

# [비트 연산을 활용한 심화 풀이]
"""
def solution_bit(n, a, b):
    # 토너먼트의 대진 구조는 이진 트리(Binary Tree)와 구조적으로 동일하여 비트 연산으로 해결 가능합니다.
    # (a-1)과 (b-1)의 XOR 연산 결과에서 가장 큰 비트의 위치가 두 참가자가 갈라지는 깊이를 나타냅니다.
    # ^ (XOR): 두 숫자의 비트가 달라지는 지점을 1로 표시하여 차이를 식별합니다.
    # .bit_length(): 달라진 비트의 길이를 통해 라운드 수를 즉시 계산합니다.
    return ((a - 1) ^ (b - 1)).bit_length()
"""
