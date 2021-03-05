def maximum(x):
    lst = []
    while x >= 1:
        rest = x % 10
        x /= 10
        lst.append(int(rest))
    lst.sort()
    print(lst)
    maximum = 0
    for i in range(len(lst)):
        maximum += lst[i] * (10 ** i)
    return maximum


def minimum(x):
    lst = []
    while x >= 1:
        rest = x % 10
        x /= 10
        lst.append(int(rest))
    lst.sort(reverse=True)
    print(lst)
    minimum = 0
    for i in range(len(lst)):
        minimum += lst[i] * (10 ** i)
    return minimum


N, K = map(int, input().split())

x = N
for i in range(K):
    x = maximum(x) - minimum(x)
print(x)
