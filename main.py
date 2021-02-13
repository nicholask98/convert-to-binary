x = int(input('enter a number to convert to binary'))

while x > 0:
    print((x % 2), end = '')
    x = x // 2
print()