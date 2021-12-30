a, b, c, k = map(int, input().split())
if k <= a:
    print(k)
elif k <= a + b:
    print(a)
elif k <= a + b + c:
    num = k - a - b
    print(a - num)
else:
    print(a - c)