
n, y = map(int, input().split())

def bills(n, y):
    flag = True
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            if (10000 * i) + (5000 * j) + (1000 * k) == y:
                print(i, j, k)
                exit()
            else:
                flag = False

    if flag == False:
        print(-1, -1, -1)

bills(n, y)