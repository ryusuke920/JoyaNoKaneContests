n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 2):
    bool = True
    for j in range(3):    
        if a[i + j][0] != a[i + j][1]:
            bool = False
    
    if bool:
        exit(print('Yes'))

print('No')