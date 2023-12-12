#deque
# 다른 풀이
# n = int(input())
# if n <= 2:
#     print(n)
# else:
#     num = 2
#     while num < n:
#         num *= 2
#     num /= 2
#     print((int)(n-num)*2)

# ** queue 풀이 **
# 일반 배열의 .pop(0) 보다 deque의 .popleft() 가 더 빠름
from collections import deque
n = int(input())
card = deque()
for i in range(1, n+1):
    card.append(i)
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(card[0])
