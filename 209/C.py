n = int(input())
c = list(map(int, input().split()))
c.sort()
div = 10**9+7
cnt = 1
for i in range(n):
    cnt *= max(0, (c[i]-i))
    cnt %= div
print(cnt)
