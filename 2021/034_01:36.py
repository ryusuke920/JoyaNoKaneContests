a, b = input().split()
num = int(a + b)
for i in range(1000):
    if i ** 2 == num:
        exit(print('Yes'))

print('No')