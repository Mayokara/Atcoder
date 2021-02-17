a, b, c, d = map(int, input().split())

if b >= d:
    end = d
else:
    end = b

if a >= c:
    start = a
else:
    start = c

time = end - start
if time >= 0:
    print(time)
else:
    print(0)