s = input()
cnt = 0
for i in s:
    if i.isnumeric():
        if int(i) != 0:
            cnt = cnt + int(i) + 2
        else:
            cnt += 12
print(cnt*2)