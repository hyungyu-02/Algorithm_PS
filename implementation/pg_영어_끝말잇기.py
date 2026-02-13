# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []

    used_words = set()
    used_words.add(words[0])
    
    for i in range(1, len(words)):
        if words[i] in used_words or words[i-1][-1] != words[i][0]:
            return [i%n + 1, i//n + 1]
        
        used_words.add(words[i])
        
    return [0, 0]
