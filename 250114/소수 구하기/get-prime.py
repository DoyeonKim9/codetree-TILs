n = int(input())

for i in range(2, n+1):
    val = 0
    for j in range(1, i+1):
        if i % j == 0:
            val += 1
    if val == 2:
        print(i, end =" ")
            

