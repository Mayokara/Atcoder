# n進数表記の数を10進数に変換
# 二分探索

x = input()
m = int(input())

# xに含まれる最大値を出す
x_list = sorted([int(i) for i in x], reverse=True)
d = x_list[0]

# n進法表記から10進法にする関数（int(x, n)だと2<=n<=36までしか対応せず）
def convert(base):
    deci = 0
    for i, e in enumerate(x[::-1]): # [::-1]　全ての要素を逆向きに得る
        deci += int(e) * (base ** i)
    return deci

if len(x) == 1: # 反省：xが一文字のときの場合分けできておらず　
    if int(x) <= m:
        print(1)
    else:
        print(0)
    exit()

# else:
#     while int(x, n) <= m:
#         n += 1
#         cnt += 1

#     print(cnt)

################################################################

else:
    lower = d
    upper = 2 * (10 ** 18)
    while upper - lower > 1:
        mid = (lower + upper) // 2
        if convert(mid) <= m:
            lower = mid
        else:
            upper = mid
    print(lower - d)


