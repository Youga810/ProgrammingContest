N = int(input())
out = -1
for i in range(N):
    A,P,X = map(int,input().split())
    if(X - A <= 0):
        continue
    else:
        if(out > P or out == -1):
            out = P
print(out)