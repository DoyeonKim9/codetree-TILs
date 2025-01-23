arr = list(map(int, input().split()))
arr1 =[]
for i in arr:
    if i % 2 == 1:
        i += 3
    else:
        i = i // 2
    arr1.append(i)
    if i == 0:
        break
        arr1.pop()
for j in arr1:
    print(j, end=" ")