n, s = input().split()
n = int(n)

ans = 0
for i in range(n - 1):
    at, cg = 0, 0
    for j in range(i, n):
        if s[j] == 'A':
            at += 1
        elif s[j] == 'T':
            at -= 1
        elif s[j] == 'C':
            cg += 1
        elif s[j] == 'G':
            cg -= 1
    
        if at == 0 and cg == 0:
            ans += 1

print(ans)