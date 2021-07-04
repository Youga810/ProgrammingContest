import math
p = int(input())
cnt = 0
coin_lst = [math.factorial(i) for i in range(10, 0, -1)]
for i in coin_lst:
    cnt += int(p / i)
    p = p % i

print(cnt)
