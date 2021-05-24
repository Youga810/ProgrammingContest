n = int(input())
a = list(map(int, input().split()))
t, q = map(int, input().split())
for i in range(q):
    x, k = map(int, input().split())
    t = t - a[x-1] * k if t - a[x-1] * k >= 0 else t
print(t)
