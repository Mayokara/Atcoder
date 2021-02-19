n = int(input())
a = [int(input()) for _ in range(n)]

# a_pushed = [0 for _ in range(n)] #ボタンiが押された回数
# cnt = 0 # 総プッシュ回数
# now = 1 # 光っているボタン

# for i in range(n):
#     a_pushed[i] += 1
#     cnt += 1
#     now = a[now - 1]
#     if now == 2:
#         print(cnt)
#     for j in range(n):
#         # (何らかのボタンが２回以上押されてる & ボタン2が押されてない) → ループ状態
#         if now != 2 and a_pushed[j] > 1: 
#             print(-1)
#             break

#         exit()
# print(-1)

pushed = [False for _ in range(n)]  # 1~n番目のボタンがそれぞれすでに押されたかどうかのフラグ（サイズn）
count = 0  # ボタンを押した回数
l_idx = 1  # 現在光っているボタンの番号（1は始まり）

while True:  # 終了条件を満たすまで無限ループ、高々n回のループまでにどちらかの条件を必ず満たす
    if l_idx == 2:  # 終了条件1: ボタン２に到達
        print(count)
        exit()
    if pushed[l_idx-1] is True:  # 終了条件2: 既に押したボタンが再度光っている事象に遭遇した場合
        print(-1)
        exit()
    pushed[l_idx-1] = True  # l_idx番のボタンを押したフラグを立てる
    l_idx = a[l_idx-1]  # 現在光っているボタン番号を切り替える
    count += 1  # インクリメント




