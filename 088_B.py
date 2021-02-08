
n = int(input())
# 入力されたaをリストにして降順にソート
list_a = list(map(int, input().split()))
list_a.sort(reverse=True)

def dif_points(list_a):
    res = 0
    A_flag = 1
    for i in list_a:
        if A_flag == 1:
            res += i
            A_flag -= 1

        else:
            res -= i
            A_flag += 1

    return res

print(dif_points(list_a))


