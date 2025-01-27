n = int(input())
arr = list(map(int, input().split()))
max_val = 0
arr1 = []
for i in arr:
    if i > max_val:
        max_val = i
        arr1.append(i)
    else:
        arr1.append(0)
for j in range(n-1, -1, -1):
    if arr1[j] != 0:
        print(j+1, end =" ")


