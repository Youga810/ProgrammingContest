H, W = map(int, input().split())
a = [list(map(int, input().split())) for l in range(H)]
l = [0 for i in range(H)]
for num1, elem in enumerate(a):
    for num2, j in enumerate(elem):
        A = sum(elem[0:num2])
        B = sum(elem[num2:])
        if(A == B):
            out = ["".join("A" for i in range(num2))]
            out2 = ["".join("B" for j in range(W-num2))]
            l[num1] = "".join(out+out2)
            break
if(len(l) == H and 0 not in l):
    print('Yes')
    for i in l:
        print(i)
else:
    print('No')
