n, a, b = map(int, input().split())

if a > b:
    print(0)
elif a == b:
    print(1)
elif a < b:
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n > 3:
        mi = a * (n - 1) + b
        ma = a + b * (n - 1)
        print(ma - mi + 1)