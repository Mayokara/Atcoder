# bit 全探索

# a, b, c, d = map(int,input())

# if a + b + c + d == 7:
#     text = '{}+{}+{}+{}=7'
#     print(text.format(a, b, c, d))
#     exit()
# elif a + b + c - d == 7:
#     text = '{}+{}+{}-{}=7'
#     print(text.format(a, b, c, d))
#     exit()
# elif a + b - c + d == 7:
#     text = '{}+{}-{}+{}=7'
#     print(text.format(a, b, c, d))
#     exit()
# elif a + b - c - d == 7:
#     text = '{}+{}-{}-{}=7'
#     print(text.format(a, b, c, d))
#     exit()
# elif a - b + c + d == 7:
#     text = '{}-{}+{}+{}=7'
#     print(text.format(a, b, c, d))
#     exit()
# elif a - b + c - d == 7:
#     text = '{}-{}+{}-{}=7'
#     print(text.format(a, b, c, d))
#     exit()
# elif a - b - c + d == 7:
#     text = '{}-{}-{}+{}=7'
#     print(text.format(a, b, c, d))
#     exit()
# elif a - b - c - d == 7:
#     text = '{}-{}-{}-{}=7'
#     print(text.format(a, b, c, d))
#     exit()

################################################################

s = [i for i in input()]
n = len(s) - 1

for i in range(1 << n):
    l = ''
    for j in range(n):
        if (i >> j) & 1:
            l += s[j] + '+'
        else:
            l += s[j] + '-'
    l += s[-1]
    if  eval(l) == 7:
        print(l + '=7')
        exit()

