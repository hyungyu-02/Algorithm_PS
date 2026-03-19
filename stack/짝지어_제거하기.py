# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    return 0 if stack else 1

# 안좋은 풀이
def solution(s):
    pointer = 0
    
    while True:
        if pointer > len(s) -2 or len(s) == 0 :
            break
        
        if s[pointer] == s[pointer + 1]:
            s = s[:pointer] + s[pointer + 2:] # 파이썬에서 문자열을 자르고 합칠 때마다 새로운 문자열 객체를 생성하며 O(N)의 시간이 걸림
            pointer = 0 # 짝을 찾을 때마다 처음부터 다시 검사하기 때문에, 최악의 경우 시간 복잡도가 O(N^2)까지 치솟아 100만 개의 문자를 처리하기엔 너무 무거움
        else:
            pointer += 1
        
    return 1 if len(s) == 0 else 0
