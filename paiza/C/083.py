n, r = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
maxNum = max(a)
loopNum = maxNum/r
for i, elem in enumerate(a):
    print(i + 1,  ':', sep='', end="")
    for j in range(int(elem/r)):
        print('*', end="")
    for j in range(int(loopNum - elem/r)):
        print('.', end="")
    if a[-1] == elem:
        break
    else:
        print()
