a, b, c = map(int, input().split())

# aとbの最大公約数求める関数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

# aをbで割った時の余りのループ周期
n = b // gcd(a, b)

for i in range(1, n + 1):
    if (i * a) % b == c:
        print('YES')
        exit()

print('NO')
