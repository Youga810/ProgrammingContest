n = input()
flag = False
for i in range(10):
    s = '0' * i + n
    if s == s[::-1]:
        flag = True
        break
if flag:
    print('Yes')
else:
    print('No')
