from itertools import product

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in product([0, 1, 2], repeat=n):
    bool = False
    for j in range(n):
        if i[j] == 0:
            num = a[j] - 1
        elif i[j] == 1:
            num = a[j]
        elif i[j] == 2:
            num = a[j] + 1
        
        if num % 2 == 0:
            bool = True

    if bool:
        ans += 1

print(ans)