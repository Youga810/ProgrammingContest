N, X = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in A:
    if i == X:
        continue
    else:
        B.append(i)
for i in range(len(B)):
    if i == len(B)-1:
        print(str(B[i])+" ")
    else:
        print(str(B[i]))
