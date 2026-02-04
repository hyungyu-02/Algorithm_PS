# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    diff = sum(numbers) - target
    if diff < 0 or diff%2 != 0:
        return 0

    minus = diff // 2

    def dfs(total, depth):
        nonlocal answer

        if depth == len(numbers) - 1:
            if total == minus:
                answer += 1
            return

        dfs(total + numbers[depth+1], depth + 1)
        dfs(total, depth + 1)
        return

    dfs(0, 0)
    dfs(numbers[0], 0)

    return answer

# 정석 풀이
"""
def solution(numbers, target):
    
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    # 0번 인덱스부터 합계 0으로 탐색을 시작합니다.
    return dfs(0, 0)
"""
