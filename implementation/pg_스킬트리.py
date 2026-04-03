# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    l = len(skill)
    for st in skill_trees:
        p = 0
        able = True
        for s in st:
            if l <= p:
                break
            if s in skill:
                if s == skill[p]:
                    p += 1
                else:
                    able = False
                    break
        
        if able:
            answer += 1
        
    return answer
