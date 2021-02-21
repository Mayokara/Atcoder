# 

n = int(input())
list_d = []
# n個の直径の入力をリストにして、降順にソート
for i in range(n):
    list_d.append(int(input()))
list_d.sort(reverse=True)

# 1つ前の要素より大きかったらres += 1
res = 1
for i in range(1, n):
    if list_d[i] < list_d[i-1]:
        res += 1

print(res)

#list_dをset型に変換して重複要素をなくしてもいいかも