a1, a2, a3 = map(int, input().split())
a = [a1, a2, a3]
a.sort()
if(a[2] - a[1] == a[1] - a[0]):
    print('Yes')
else:
    print('No')
