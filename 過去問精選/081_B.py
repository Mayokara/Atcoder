# ABC081_B

n = int(input())
A = list(map(int, input().split()))

# 各要素が2で割り切れる回数をリスト化 → 最小値表示
cnt = [0]*len(A)
for i in range(len(A)):
    a = A[i]
    while a % 2 == 0:
        cnt[i] += 1
        a = a // 2    

print(min(cnt))

# 割り切れないものが出たところでやめる