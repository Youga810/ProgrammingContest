a, b, c = map(int, input().split())
n = [a, b, c]
sum = 0
for i in range(3):
    sum += 7 - n[i]

print(sum)
