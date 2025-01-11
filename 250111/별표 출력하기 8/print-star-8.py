for i in range(6):
    if i % 2 == 1:
        for j in range(i+1):
            print("*", end =" ")
        print()
    else:
        print("*")