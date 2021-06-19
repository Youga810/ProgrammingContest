import math
n = int(input())

n = math.floor(1.08 * n)
if n < 206:
    print('Yay!')
elif n == 206:
    print('so-so')
else:
    print(':(')
