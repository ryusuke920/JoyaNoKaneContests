from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in permutations([i + 1 for i in range(n - 1)]):
    dist = 0
    p = [0] + list(i) + [0]
    for j in range(n):
        dist += t[p[j]][p[j + 1]]
    
    if dist == k:
        ans += 1

print(ans)