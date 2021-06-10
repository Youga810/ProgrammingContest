n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append([i+1, i+1])

for i in range(m):
    tempa, tempb = map(int, input().split())
    lst.append([tempa, tempb])


for i in lst:
    tempa = i[0]
    tempb = i[1]
    for j in lst:
        if tempb == j[0] and [tempa, j[1]] not in lst:
            lst.append([tempa, j[1]])

arr = list(map(list, set(map(tuple, lst))))
# todo最後に同じの消す
print(len(arr))
