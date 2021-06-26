n = int(input())
lst = []
for i in range(n):
    t,l,r = map(int,input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        r -= 0.1
        l += 0.1
    lst.append([l,r])
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if lst[i][1] >= lst[j][0]:
            cnt += 1
print(cnt)