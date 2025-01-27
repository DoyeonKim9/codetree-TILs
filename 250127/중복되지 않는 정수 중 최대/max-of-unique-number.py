n = int(input())
arr = list(map(int, input().split()))
cnt = 0
arr1 = []
for i in range(n):
    if arr[i] in arr1:
        continue
    if arr[i] in arr[i+1:]:
        arr1.append(arr[i])
        continue
    if arr[i] > cnt:
        cnt = arr[i]

if cnt == 0:
    print("-1")
else:
    print(cnt)
