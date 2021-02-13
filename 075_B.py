h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

# ↑ → ↓ ← 
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(h):
    for j in range(w):
        cnt = 0
        if s[i][j] == '#':
            for k in range(len(dx)):
                x = i + dx[k]
                y = j + dy[k]
                cnt += 1
                s[i][j] = cnt



# cnt = ['0' * w] * h

# for i in range(h):
#     for j in range(w):
#         if s[i][j] == '#':
#             cnt[i-1][j] += 1
#             cnt[i+1][j] += 1
#             s[i][j-1] += 1
#             s[i][j+1] += 1
#             s[i-1][j-1] += 1
#             s[i-1][j+1] += 1
#             s[i+1][j-1] += 1
#             s[i+1][j+1] += 1


# for i in range(h):
#     print(s[i])
