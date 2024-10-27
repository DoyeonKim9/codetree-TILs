a, b, c = map(int, input().split())

if a <= b <= c or b <= a < c:
    print(c)
elif a <= c <= b or c <= a <= b:
    print(b)
else:
    print(a)