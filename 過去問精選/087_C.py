# 累積和
n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

total = [0 for _ in range(n)]

ans = -1
for i in range(n):
    total[i] = sum(a[0][:(i + 1)]) + sum(a[1][i:])
    if ans < total[i]:
        ans = total[i]

print(ans)

cum_0 = a[0][0]
cum_1 = a[0][0] + a[1][0]
for i in range(1, n):
    cum_0 += a[0][i]
    if a[]































