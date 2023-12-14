#DP(동적계획법)
import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

cache = [0]*len(word2)

for i in word1:
    cnt = 0
    for j in range(len(cache)):
        if cnt < cache[j]:
            cnt = cache[j]
        elif i == word2[j]:
            cache[j] = cnt + 1

print(max(cache))
