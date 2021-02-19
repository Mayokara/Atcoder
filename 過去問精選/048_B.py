a, b, x = map(int, input().split())

cnt_b = b // x
cnt_a = (a - 1) // x
ans = cnt_b - cnt_a

print(ans)
# cnt = 0
# for i in range(a, b + 1):
#     if i % x == 0:
#         cnt += 1

# print(cnt)