n = int(input())
x = list(map(int, input().split()))
a, b, c = 0, 0, 0
for i in range(n):
    a += abs(x[i])
    b += x[i] ** 2
    c = max(c, abs(x[i]))

print(a)
print(b ** 0.5)
print(c)