h, w, y, x = map(int, input().split())
s = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    line = input()
    for j in range(w):
        s[i][j] = line[j]
x -= 1
y -= 1
cnt = 1
temp = cnt
i = x
j = x
k = y
l = y
while(True):
    # 左
    if i != 0 and s[y][i-1] != '#':
        cnt += 1
        i -= 1
    # 上
    if k != 0 and s[k - 1][x] != '#':
        cnt += 1
        k -= 1
    # 右
    if j != w-1 and s[y][j+1] != '#':
        cnt += 1
        j += 1
    # 下
    if l != h-1 and s[l+1][x] != '#':
        cnt += 1
        l += 1
    if temp == cnt:
        break
    temp = cnt

print(cnt)
