# 10進数をn進数に変換
# 二分探索

x = input()
m = int(input())

# xに含まれる最大値を出す
x_list = sorted([int(i) for i in x], reverse=True)
d = x_list[0]

n = d + 1
cnt = 0

if len(x) == 1: # 反省：xが一文字のときの場合分けできておらず　
    if int(x, n) <= m:
        cnt = 1
    else:
        cnt = 0
    print(cnt)
    exit()

else:
    while int(x, n) <= m:
        n += 1
        cnt += 1

    print(cnt)


