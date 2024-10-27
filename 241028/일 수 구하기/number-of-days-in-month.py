n = int(input())

if n == 2:
    print("28")
elif n < 8:
    if n % 2 == 1:
        print("31")
    else:
        print("30")
else:
    if n % 2 == 1:
        print("30")
    else:
        print("31")