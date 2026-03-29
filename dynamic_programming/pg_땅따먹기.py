# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0
    
    for r in range(1, len(land)):
        sorted_indices = sorted(enumerate(land[r-1]), key=lambda x: x[1], reverse=True) # 이전 행을 (인덱스, 값) 구조로 내림차순 정렬
        for c in range(4):
            land[r][c] += sorted_indices[0][1] if c != sorted_indices[0][0] else sorted_indices[1][1]
    
    return max(land[-1])
