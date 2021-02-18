n, k = map(int, input().split())

ans = k * (k - 1) ** (n - 1)

print(ans)

# pow(a, b) == a ** bを使ってもよし
# pow(a, b, c) == (a ** b) % c　と第３引数を取れる。余りを出すのであれば演算子より組み込み関数powのが早い。