# for文 全探索
# 平方根

import math

n = int(input())
c = [list(map(int,input().split())) for _ in range(n)]

ans_2 = 0
for i in range(n):
    for j in range(n):
        l = (c[j][0] - c[i][0])**2 + (c[j][1] - c[i][1])**2
        if ans_2 < l:
            ans_2 = l

print(math.sqrt(ans_2))