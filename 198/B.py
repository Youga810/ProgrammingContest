def palindrome(n):
    for i in range(int(len(n) / 2)):
        if n[i] != n[-1]:
            return False
    return True


n = input()
n_len = len(n)
for i in range(0, 9):
    flag = palindrome('0'*i + n)
    if flag:
        break
if flag:
    print('Yes')
else:
    print('No')
