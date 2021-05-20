import operator

n = int(input())
st = [input().split() for j in range(n)]

sortedItem = sorted(st, key=operator.itemgetter(1))
print(sortedItem[-2][0])
