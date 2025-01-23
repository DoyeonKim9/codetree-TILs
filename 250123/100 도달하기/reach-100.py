n = int(input())


arr = [1, n]

for i in range(100):
    arr.append(arr[i] + arr[i+1])
for j in arr:
    print(j, end=" ")
    if j >= 100:
        break