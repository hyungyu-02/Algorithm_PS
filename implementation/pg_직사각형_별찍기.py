# https://school.programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))

row = '*' * a

for _ in range(b):
    print(row)
