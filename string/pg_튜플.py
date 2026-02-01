# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    
    s = s[2:-2].split('},{')
    
    data = []
    
    for st in s:
        data.append(list(map(int, st.split(','))))
    
    data.sort(key=len)
    
    answer = []
    
    for d in data:
        for num in d:
            if num not in answer:
                answer.append(num)
                break
    
    return answer
