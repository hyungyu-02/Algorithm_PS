# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    answer = 0

    is_searched = [False for _ in range(n)]

    def bfs(start_node):
        queue = deque([start_node])
        is_searched[start_node] = True

        while queue:
            x = queue.popleft()

            for j in range(n):
                if computers[x][j] == 1 and not is_searched[j]:
                    queue.append(j)
                    is_searched[j] = True

    for i in range(n):
        if not is_searched[i]:
            bfs(i)
            answer += 1

    return answer

# [DFS 풀이]
"""
def dfs(i, n, computers, visited):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:
            dfs(j, n, computers, visited)

# 메인 로직에서 bfs(i) 대신 dfs(i, n, computers, visited) 호출 시 동일하게 작동함
# 네트워크 개수 파악 등 단순 연결성 확인에는 DFS가 구현이 더 간결하여 선호되기도 함
"""
