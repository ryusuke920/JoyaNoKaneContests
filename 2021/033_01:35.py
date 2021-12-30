from collections import Counter
n = int(input())
s = [input() for _ in range(n)]

ans = Counter(s).most_common()
print(ans[0][0])