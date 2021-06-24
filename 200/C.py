n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
a = [i % 200 for i in a]
s = dict()
for i in a:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1
sum = 0
for key, val in s.items():
    sum += int(val * (val-1) / 2)

print(sum)
