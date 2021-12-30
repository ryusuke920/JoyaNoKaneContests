n = int(input())
a = list(map(int, input().split()))

b = []
for i in a:
    b.append(i)

b.sort()
num = b[-2]
for i, j in enumerate(a):
    if j == num:
        exit(print(i + 1))