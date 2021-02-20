# 各桁の数字を並び替え
# 数値→文字列変換してソートし、数値に戻す 

# 反省：文字列からソートされたリストを生成できることを知らなかった。
# a = '1452'
# print(sorted(a))
# ['1', '2', '4', '5']

n, k = input().split()

def list_(n):
    l_n = list(n)
    l = [int(i) for i in l_n]
    return l

def g1(l):
    l.sort(reverse=True)
    l_str = [str(i) for i in l]
    l1 = ''.join(l_str)
    l1_int = int(l1)
    return l1_int

def g2(l):
    l.sort()
    l_str = [str(i) for i in l if str(i) != "0"] # 反省：str(i) != 0 で最初やってた
    if len(l_str) == 0: # 反省：n = 0のとき空のリストになることを考えてなかった
        return 0
    l2 = ''.join(l_str)
    l2_int = int(l2)
    return l2_int

if int(k) == 0: # 反省：k = 0のときを考えてなかった
    print(n)
    exit()
else:
    l = list_(n)
    for i in range(int(k)):
        a = g1(l) - g2(l)
        a_str = str(a)
        l = list_(a_str)

    print(a)

################################################
