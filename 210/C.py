n, k = map(int, input().split())
c = list(map(int, input().split()))
cnt = 0
for i in range(n - k + 1):
    s = set(c[i:i+k])
    if cnt < len(s):
        cnt = len(s)
print(cnt)
