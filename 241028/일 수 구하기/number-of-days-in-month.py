n = int(input())

if n % 2 == 1 and n < 8:
    print("31")
else:
    if n == 8: 
        print("31")
    elif n > 8 and n % 2 == 1:
        print("30")
    else:
        print("28")