s = list(input())
t = list(input())

l = len(s)
for i in range(1000):
    x = s[-1]
    s = s[:l - 1]
    s = [x] + s

    if s == t:
        exit(print('Yes'))

print('No')