n = int(input())
arr1 = []
arr = list(map(int, input().split()))
for i in arr:
    if i % 2 == 0:
        arr1.append(i)
for k in arr1[::-1]:
    print(k, end =" ")
