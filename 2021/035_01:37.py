n = int(input())
ans = set()
for a in range(2, 10 ** 6):
    b = 2
    while a ** b <= n:
        if 1 <= a ** b <= n:
            ans.add(a ** b)
        b += 1

print(n - len(ans))