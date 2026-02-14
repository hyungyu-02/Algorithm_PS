# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    dictionary = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current_word):
        if len(current_word) > 5:
            return
        
        if current_word:
            dictionary.append(current_word)
        
        for vowel in vowels:
            dfs(current_word + vowel)
    
    dfs("")
    
    return dictionary.index(word) + 1
