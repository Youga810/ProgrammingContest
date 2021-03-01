s = list(str(input()))
dif = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
out = list(filter(lambda i: i not in dif, s))
print("".join(out))
