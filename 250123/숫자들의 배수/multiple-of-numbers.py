n = int(input())
arr1 = []
cnt = 0
for i in range(1, 11):
    arr1.append(n*i)
    if n * i % 5 == 0:
        cnt += 1
        if cnt == 2:
            break
    
for j in arr1:
    print(j, end=" ")