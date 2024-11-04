n = int(input())
j1 = 0
for i in range(1, n+1):
    j1 = 0
    if i % 3 == 0:
        print("0", end = ' ')
    else:
        for j in str(i):
            if j == '3' or j == '6' or j =='9':
                j1 = 1
        if j1:
            print(0, end = ' ')
        else: 
            print(i, end = " ")