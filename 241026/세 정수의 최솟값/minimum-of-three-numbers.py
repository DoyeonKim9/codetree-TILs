a, b, c = map(int, input().split())

if a <= b <= c or a <= c <= b:
    print(a)
elif b <= a <= c or b <= c <= a:
    print(b)
else:
    print(c)