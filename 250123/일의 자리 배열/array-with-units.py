arr = list(map(int, input().split()))

for i in range(8):
    arr.append(arr[-1] + arr[-2])

for j in arr:
    if j > 9:
        j = j % 10
    print(j, end =" ")

