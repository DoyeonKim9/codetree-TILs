n = int(input())
x = n
y = 0
for i in range(n*2):
    if i % 2 == 0:
        for j in range(x, 0, -1):
            print("*", end = " ")
        x -= 1
        print()
    else:
        y += 1
        for j in range(y):
            print("*", end = " ")
        print()
        