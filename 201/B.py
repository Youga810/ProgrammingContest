n = int(input())
st = [input().split() for j in range(n)]

sortedItem = sorted(st, key=lambda x: int(x[1]), reverse=True)
print(sortedItem)
