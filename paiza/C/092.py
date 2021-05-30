n, a, b = map(int, input().split())
sn = input()
sa = input()
sb = input()
tempsn = sn
lena = len(sa)
lenb = len(sb)

for i in sa:
    if i in sn:
        index = sn.find(i)
        if index + 1 < lena:
            sn = sn[index+1:]
        print('index', index)
        print('sn', sn)
