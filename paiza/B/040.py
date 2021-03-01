n, T = input().split()
alphab = [chr(i) for i in range(97, 123)]
n = int(n)
s = input().split()
length = len(s)
for j in range(n):
    for num, elem in enumerate(s):
        for i in elem:
            elem += alphab[T.index(i)]
            elem = elem[1:]
            # elem.join(T.index(i))
            # elem.pop()
            s[num] = elem

for i, elem in enumerate(s):
    if(i == len(s)-1):
        print(elem, end="")
    else:
        print(elem, end=" ")
