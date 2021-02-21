# パリティ
# 英小文字、大文字判定

s = input()

for i in range(0, len(s)):
    if i % 2 == 0 and s[i].islower() is False:
        print('No')
        exit()

    elif i % 2 == 1 and s[i].isupper() is False:
        print('No')
        exit()

print('Yes')



