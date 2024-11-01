a, b = map(int, input().split())

if a > 0:
    for _ in range(1, b+1):
        print(a, end ="")
else:
    print("0")