n, a, b = map(int, input().split())
sn = input()
sa = input()
sb = input()
tempsn = sn

for i in sa:
    if i in sn:
        index = sn.find(i)
        sn = sn[index+1:]
        print('index', index)
        print('sn', sn)
