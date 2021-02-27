N = int(input())
cnt = 0
for i in range(1,N+1):
    flag = False
    for b in range(2,N):
        for a in range(2,N):

            if(i == a**b):
                #print("i:",i,a,b)
                flag = True
                break
            if(i > a**b):
                #print("超過:",i,a,b)
                break
            else:
                continue
        if(flag):break
    if(flag == False):cnt=cnt+1
print(cnt)