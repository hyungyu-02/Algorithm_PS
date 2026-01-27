# https://school.programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 수동 Dictionary 구현 방식
"""
def solution_manual(participant, completion):

    hash_dict = {}
    
    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1 
        # .get()에서 p가 hash_dict에 있으면 해당 value를, 없으면 0을 반환
        
    for c in completion:
        hash_dict[c] -= 1
        
    for key in hash_dict:
        if hash_dict[key] > 0:
            return key
"""
