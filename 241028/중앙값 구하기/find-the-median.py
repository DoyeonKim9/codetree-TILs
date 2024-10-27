a, b, c = map(int, input().split())

if a < b:
    if b < c:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)
else:
    if a < c:
        print(a)
    else:
        if b > c:
            print(b)
        else:
            print(c)