n = int(input())
cnt = 0
i = 0
while True:
    i += 1
    if(len(str(i)) % 2 != 0):
        i = i * 10

        continue
    half = int(len(str(i)) / 2)
    hoge = str(i)
    if(hoge[:half] == hoge[half:]):
        cnt += 1
    if(i >= n):
        break
print(cnt)
