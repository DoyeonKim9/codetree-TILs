n = int(input())
for i in range(0, 2*n, 2):
    for j in range(11, 11 + n*2, 2):
            print(j+i, end = " ")
    print()