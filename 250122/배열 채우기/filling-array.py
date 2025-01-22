
arr = list(map(int, input().split()))
arr1 = list()

for i in arr:
    if i == 0:
        break
    arr1.append(i)
for j in arr1[::-1]:
    print(j, end =" ")

    