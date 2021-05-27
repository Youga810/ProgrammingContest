h, w, x, y = map(int, input().split())
s = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    line = input()
    for j in range(w):
        s[i][j] = line[j]
x -= 1
y -= 1
cnt = 0
