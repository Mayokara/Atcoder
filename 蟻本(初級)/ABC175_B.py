# for文 全探索
# 三角形成立条件

n = int(input())
l = sorted(map(int, input().split()))

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if l[i] == l[j]:
            continue
        for k in range(j + 1, n):
            if l[j] == l[k]:
                continue
            elif (l[i] + l[j]) > l[k]:
                cnt += 1

print(cnt)