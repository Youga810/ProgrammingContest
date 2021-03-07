n = int(input())
a = [0] * n
b = [0] * n
time = 200001

for i in range(n):
    a_num, b_num = map(int, input().split())
    a[i] = a_num
    b[i] = b_num

for i, elem1 in enumerate(a):
    for j, elem2 in enumerate(b):
        if(i == j):
            time = min(time, elem1 + elem2)
        else:
            time = min(time, max(elem1, elem2))
print(time)
