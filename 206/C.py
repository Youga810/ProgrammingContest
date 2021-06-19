n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
sum = int(n * (n-1) / 2)
b = {}
for i in range(n):
    if a[i] not in b:
        b[a[i]] = 1
    else:
        b[a[i]] += 1
for val in b.values():
    sum -= int(val * (val-1) / 2)
print(sum)
