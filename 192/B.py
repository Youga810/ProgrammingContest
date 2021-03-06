S = input()
flag = True
for i, elem in enumerate(S):
    if(i % 2 == 0 and elem.isupper()):
        flag = False
    if(i % 2 == 1 and elem.islower()):
        flag = False

if(flag):
    print('Yes')
else:
    print('No')
