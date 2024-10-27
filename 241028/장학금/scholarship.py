mid, fin = map(int, input().split())

if mid >= 90:
    if fin >= 95:
        print("10")
    elif fin >= 90:
        print("5")
    else:
        print("0")
else:
    print("0")