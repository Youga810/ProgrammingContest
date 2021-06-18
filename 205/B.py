n = int(input())
a = list(map(int, input().split()))
b = list(range(1, n+1))
a = sorted(a)
if a == b:
    print('Yes')
else:
    print('No')
