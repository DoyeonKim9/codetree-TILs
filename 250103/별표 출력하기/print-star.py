n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
    print()

for i in range(0, n, 1):
    for j in range(n - i -1):
        print("*", end = " ")
    print()