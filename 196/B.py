import math

x = input()
if(x.find('.') != -1):
    num = x.find('.')
    x = x[0:num]
print(math.floor(int(x)))
