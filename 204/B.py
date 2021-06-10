n = int(input())
a = list(map(int, input().split()))

sum = 0
for i in a:
    if i > 10:
        sum += i - 10
print(sum)
