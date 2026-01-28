# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    
    days = []
    for p, s in zip(progresses, speeds):
        days.append(-( (p - 100) // s ))
    # 수학적 계산을 통해 O(N) 의 복잡도로 최적화
    
    release_day = days[0]
    count = 0
    
    for d in days:
        if d > release_day:
            answer.append(count)
            release_day = d
            count = 1
        else:
            count += 1
    
    answer.append(count)
    return answer

# 원래 생각했던 풀이
"""
def solution(progresses, speeds):
    answer = []
    
    progressNum = len(progresses)
    
    while True:
        if progresses[0] >= 100:
            count = 0
            for p in progresses:
                if p >= 100:
                    count += 1
                else:
                    break
            answer.append(count)
            progresses = progresses[count:]
            speeds = speeds[count:]
            progressNum -= count
        
        if progressNum <= 0:
            break
        
        for i in range(progressNum):
            progresses[i] += speeds[i]
        
        
    return answer
"""
