v, t, s, d = map(int, input().split())
if t * v <= d and s * v >= d:
    print('No')
else:
    print('Yes')
