# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(fatigue, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= fatigue:
                visited[i] = True
                dfs(fatigue - dungeons[i][1], count + 1)
                visited[i] = False
    
    dfs(k, 0)
    
    return answer
