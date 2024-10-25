a, b, c = map(int, input().split())

if b < c and a == b:
    print("1", end = " ")
elif b > c and a == c:
    print("1", end = " ")
elif a <= b <= c and a <= c <= b:
    print("1", end = " ")
else:
    print("0", end = " ")

if a == b and b == c:
    print("1")
else:
    print("0")