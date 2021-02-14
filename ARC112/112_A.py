t = int(input())

ans = [0] * t
for i in range(t):
    l, r = map(int,input().split())
    for j in range(l, r + 1):
        for k in range(l, r + 1):
            if (j + k) <= r:
                ans[i] += 1

for i in range(t):
    print(ans[i])




# for i in range(t):
#     for j in range(case[i][0], case[i][1] + 1):
#         for k in range(case[i][0], j + 1):
#             if case[i][0] <= (j - k):
#                 ans[i] += 1

# for i in range(t):
#     print(ans[i])