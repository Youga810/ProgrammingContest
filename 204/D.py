import itertools

n = int(input())
t = list(map(int, input().split()))

lst = list(itertools.permutations(t))
for i in lst:
    for j, elem in enumerate(i):
        tempa = elem[0:j]
        tempb = elem[j+1:]
