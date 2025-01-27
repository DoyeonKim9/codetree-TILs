arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    if i == 999 or i == -999:
        break
    arr1.append(i)
print(max(arr1), min(arr1))
