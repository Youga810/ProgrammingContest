n, m = map(int, input().split())
w = [input() for i in range(m)]
lst = []
for i in w:
    temp = 100000
    for j in range(int(int(i)/n) + 1):
        if temp > int(j + 1) * n - int(j + 1):
            temp = int(j+1) * n
    lst.append(temp)
print(lst)
