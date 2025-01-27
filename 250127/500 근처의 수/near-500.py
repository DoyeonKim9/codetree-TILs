arr = list(map(int, input().split()))

arr1 = []
arr2 = []

for i in arr:
    if i < 500:
        arr1.append(i)
    else:
        arr2.append(i)

print(max(arr1), min(arr2))