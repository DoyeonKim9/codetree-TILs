arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    if i == 0:
        break
    arr1.append(i)
print(arr1[-1] + arr1[-2] + arr1[-3])