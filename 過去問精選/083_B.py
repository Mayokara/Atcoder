# 10進法表記の扱い
# for文


# 各桁の和を計算
def sum_digit(num):
    t = 0
    while num > 0:
        t += num % 10
        num //= 10
    return t

n, a, b = map(int, input().split())

# 数字の各桁の和がa以上b以下のとき、resにその数字を足していく
res = 0
for i in range(1, n + 1):
    temp = sum_digit(i)
    if a <= temp <= b:
        res += i
    
print(res)
