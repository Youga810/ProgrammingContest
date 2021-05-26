
def isKaibun(n):
    for i in range(len(n)):
        if n[-i-1] != n[i]:
            return False
    return True


n = input()
while(True):
    if isKaibun(n):
        break
    reversedStr = n[::-1]
    n = int(reversedStr) + int(n)
    n = str(n)
    #  strN = str(n)[::-1]
    #  for i in strN:
    #      pass

print(n)
