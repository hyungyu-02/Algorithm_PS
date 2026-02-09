# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    cloth_hash = {}
    for cloth_name, category in clothes:
        cloth_hash[category] = cloth_hash.get(category, 0) + 1
    
    answer = 1
    for k, v in cloth_hash.items():
        answer *= (v+1)
    
    return answer - 1
