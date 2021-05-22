s = input()
s2 = []
for elem in reversed(s):
    if(elem == '6'):
        print('9', end="")
    elif(elem == '9'):
        print('6', end="")
    else:
        print(elem, end="")
