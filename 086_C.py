import sys
n = int(input())
list_txy = [[0, 0, 0]]
for i in range(n):
    list_txy.append(list(map(int, input().split())))

def route(list_txy):
    for i in range(1, n + 1):
        t = list_txy[i][0] - list_txy[i-1][0]
        x = list_txy[i][1] - list_txy[i-1][1]
        y = list_txy[i][2] - list_txy[i-1][2]
        dist = abs(x) + abs(y)
        if t >= dist:
            if t % 2 == dist % 2:
                continue
            else:
                print('No')
                sys.exit()
        else:
            print('No')
            sys.exit()

    print('Yes')

route(list_txy)

# for i in range(n):
#     t, x, y = map(int, input().split())
#     dt = t