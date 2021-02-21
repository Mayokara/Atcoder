# グリッド

h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

# ↑ → ↓ ← 
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

ans = [[0 for _ in range(w)] for _ in range(h)]
mines = []

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            for k in range(len(dx)):      
                x = j + dx[k]          
                y = i + dy[k]
                if (0 <= x < w) and (0 <= y < h) and (s[y][x] != '#'):
                    ans[y][x] += 1
            ans[j][i] = '#'
            # mines.append((j, i))

# for mine in mines:
#     ans[mine[1]][mine[0]] = '#'

print(ans)
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
