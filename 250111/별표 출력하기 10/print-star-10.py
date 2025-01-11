n = int(input())
x = 0
y = n
for i in range(n*2):
    if i % 2 == 0:
        x += 1
        for j in range(x):
            print("*", end = " ")
        print()
    else:
        y -= 1
        for j in range(y+1):
            print("*", end = " ")
        print()
    
        