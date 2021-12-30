n = int(input())
t = list(map(int ,input().split()))
time = sum(t)

for _ in range(int(input())):
    p, m = map(int, input().split())
    print(time - (t[p - 1] - m))