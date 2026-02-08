# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    puddle_set = set((y, x) for x, y in puddles)
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if x == 1 and y == 1: continue
            
            if (y, x) not in puddle_set:
                dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % 1000000007
    
    return dp[n][m]
