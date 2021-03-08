h, w = map(int, input().split())
s = [input() for i in range(h)]
p = [list(map(int, input().split())) for i in range(h)]
cnt = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            cnt += p[i][j]
print(cnt)
