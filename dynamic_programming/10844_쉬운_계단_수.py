#Dynamic Programming
n = int(input())
dp = [[0]*n for _ in range(10)]
for i in range(1,10):
    dp[i][0] = 1
for i in range(1,n):
    dp[0][i] = dp[1][i-1]%1000000000
    for j in range(1,9):
        dp[j][i] = (dp[j-1][i-1] + dp[j+1][i-1])%1000000000
    dp[9][i] = dp[8][i-1]%1000000000
ans = 0
for i in range(10):
    ans += dp[i][n-1]
    ans = ans % 1000000000
print(ans)
