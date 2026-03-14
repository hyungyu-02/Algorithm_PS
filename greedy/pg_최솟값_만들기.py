# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer

# 더 간결한 풀이
# return sum(a * b for a, b in zip(A, B))
