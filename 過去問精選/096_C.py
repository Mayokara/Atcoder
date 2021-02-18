h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

flag = True
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            flag = False
            if (0 < i < h) and (s[i - 1][j] == '#'):
                flag = True
            elif (0 <= j < (w - 1)) and (s[i][j + 1] == '#'):
                flag = True
            elif (0 <= i < (h - 1)) and (s[i + 1][j] == '#'):
                flag = True
            elif (0 < j < w) and (s[i][j - 1] == '#'):
                flag = True


if flag is True:
    print('Yes')
else:
    print('No')

    #???????