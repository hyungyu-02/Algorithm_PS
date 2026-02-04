# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    if citations[0] < 1:
        return 0
    
    for i in range(1, len(citations)):
        if i >= citations[i]:
            return i
    
    return len(citations)

# enumerate를 활용한 더 깔끔한 풀이
"""

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        if citation <= i:
            return i
    
    return len(citations)

"""
