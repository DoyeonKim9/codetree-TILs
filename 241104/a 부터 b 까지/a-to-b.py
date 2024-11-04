a, b = map(int, input())
for i in range(a, b+1):
    if i % 2 == 1:
        print(i, end = " ")
        i *= 2
    else:
        print(i, end = " ")
        i += 3