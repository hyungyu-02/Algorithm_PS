# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x]) 
            # 경로 압축(Path Compression) -> 최상위 부모를 찾으면서 동시에 parent[x] 값을 최상위 부모로 업데이트까지 해버림
        return parent[x]

    def union(parent, a, b):
        parent_of_a = find(parent, a)
        parent_of_b = find(parent, b)

        if parent_of_a > parent_of_b:
            parent[parent_of_a] = parent_of_b
        else:
            parent[parent_of_b] = parent_of_a

    edges = 0
    for a, b, cost in costs:
        if find(parent, a) == find(parent, b): continue

        union(parent, a, b)
        answer += cost
        edges += 1

        if edges == n-1: break

    return answer
