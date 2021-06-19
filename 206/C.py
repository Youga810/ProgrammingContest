import itertools
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
sum = 0
lst = []
# for i in range(1, n):
#    if a.count(i) > 1:
#        lst.append(a.count(i))
#    sum += i
# for i in lst:
#    cnt = 0
#
#    sum -= cnt
# print(sum)
#

for balls in itertools.combinations(a, 2):
    print(balls)
