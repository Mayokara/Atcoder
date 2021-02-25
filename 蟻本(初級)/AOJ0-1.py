# 動的計画法
# ナップサック問題

n, w = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
for i in range(n):
    vi, wi = goods[i][0], goods[i][1]
    for j in range(w + 1):
        if j < wi:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - wi] + vi)

print(dp[n][w])