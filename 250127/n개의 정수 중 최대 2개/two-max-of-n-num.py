n = int(input())
arr = list(map(int, input().split()))
max1, max2 = arr[0], arr[1]

if max1 > max2:
    max1, max2 = arr[0], arr[1]
else:
    max1, max2 = arr[1], aee[0]

for i in range(2, n):
    if arr[i] > max1:
        max1, max2 = arr[i], max1
    elif arr[i] > max2:
        max2 = arr[i]
print(max1, max2)
