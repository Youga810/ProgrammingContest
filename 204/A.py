x, y = map(int, input().split())
lst = [0, 1, 2]

if x != y:
    lst.remove(x)
    lst.remove(y)
    print(lst.pop())
else:
    print(x)
