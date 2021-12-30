from itertools import combinations

n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in combinations(l, 3):
    if max(i) < sum(i) - max(i):
        if len(set(i)) == 3:
            ans += 1

print(ans)