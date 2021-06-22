n = int(input())

p = n % 100
n = int(n/100)

if p != 0:
    n += 1
print(n)
