# 累積和
n = int(input())
s = input()

# cnt = [0 for _ in range(n)]
# for i in range(n):
#     for j in range(i):
#         if s[j] == 'W': # i番目より左にW向きがいる場合
#             cnt[i] += 1 # increment
#     for j in range(i + 1, n): 
#         if s[j] == 'E': # i番目より右にE向きがいる場合
#             cnt[i] += 1 # increment

# print(min(cnt))

wcnt = [0 for _ in range(n)]
ecnt = [0 for _ in range(n)]

if s[0] == 'W':
    wcnt[0] = 1
else:
    ecnt[0] = 1

for i in range(1, n):
    if s[i] == 'W':
        wcnt[i] = wcnt[i-1] + 1
        ecnt[i] = ecnt[i-1]
    elif s[i] == 'E':
        wcnt[i] = wcnt[i-1]
        ecnt[i] = ecnt[i-1] + 1

ans = 3 * (10**5) + 1

for i in range(n):
    if i == 0:
        cnd = ecnt[-1] - ecnt[0]
    else:
        cnd = wcnt[i-1] + ecnt[-1] - ecnt[i]
    if cnd < ans:
        ans = cnd

print(ans)