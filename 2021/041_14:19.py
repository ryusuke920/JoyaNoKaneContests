h, w, c, q = map(int, input().split())
tnc = [list(map(int, input().split())) for _ in range(q)][::-1]

h_col = set()
w_col = set()

color = [0] * c
for i in range(q):
    if tnc[i][0] == 1:
        if tnc[i][1] not in h_col:
            h_col.add(tnc[i][1])
            color[tnc[i][2] - 1] += w - len(w_col)
    elif tnc[i][0] == 2:
        if tnc[i][1] not in w_col:
            w_col.add(tnc[i][1])
            color[tnc[i][2] - 1] += h - len(h_col)

print(*color)