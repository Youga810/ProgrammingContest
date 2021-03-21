# ?????????????????????????

h, w = map(int, input().split())

map = []

# print(map)
for i in range(h):
    map.append(input().split())
print(map)
for i in range(h):
    for j in range(w):
        if(i == 0 or j == 0):
            print(map[i][0][j], end="")
            # print(new[i][j])
           # pass
