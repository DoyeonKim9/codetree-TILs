n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or j % 2 == 0 and i <= j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
        
