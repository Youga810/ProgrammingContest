n, m = map(int, input().split())
allCard = [i for i in range(1, m+1)]
cnt = 0
for i, elem in enumerate(range(n)):
    num = int(input())
    if num in allCard:
        allCard.remove(num)
        if len(allCard) <= 0:
            cnt = i + 1

res = cnt if cnt > 0 else 'unlucky'
print(res)
