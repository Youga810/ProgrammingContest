import math
n, k = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)
a_dict = {}
rest = k % n
for i in a:
    a_dict[i] = math.floor(k/n)
for i in sorted_a:
    if rest == 0:
        break
    else:
        a_dict[i] += 1
        rest -= 1

for v in a_dict.values():
    print(v)
