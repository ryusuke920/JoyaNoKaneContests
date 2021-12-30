n = int(input())
a = list(map(int, input().split()))

num = [0] * n
for i in range(n - 1):
    num[a[i] - 1] += 1

print(*num, sep='\n')