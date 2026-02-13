# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    sorted_priorities = sorted(priorities, reverse=True)
    
    pointer = 0
    done_count = 0
    
    while True:
        if priorities[pointer] == sorted_priorities[done_count]:
            done_count += 1
            if pointer == location:
                return done_count
        
        pointer += 1
        if pointer == len(priorities):
            pointer = 0


# queue를 이용한 정석적인 풀이

from collections import deque

def solution(priorities, location):
    # [Insight] 프로세스의 (우선순위, 원래 인덱스)를 한 쌍으로 묶어 큐에 넣습니다.
    # [Reason] 큐가 회전하더라도 원래 우리가 찾고 싶던 프로세스인지 확인하기 위함입니다.
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0

    while queue:
        # 1. 가장 앞에 있는 프로세스를 꺼냅니다.
        current = queue.popleft()
        
        # 2. 큐에 남아있는 프로세스 중 현재보다 우선순위가 높은 것이 있는지 확인합니다.
        # [Insight] any() 함수를 사용하면 가독성 있게 체크할 수 있습니다.
        if any(current[0] < p[0] for p in queue):
            # [Reason] 더 높은게 있다면 현재 프로세스를 다시 맨 뒤로 보냅니다.
            queue.append(current)
        else:
            # 3. 없다면 현재 프로세스를 실행합니다.
            answer += 1
            # [Insight] 만약 지금 실행한 프로세스가 내가 찾던(location) 것이라면 종료!
            if current[1] == location:
                return answer
