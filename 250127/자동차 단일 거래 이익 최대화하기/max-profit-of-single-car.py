n = int(input())
arr = list(map(int, input().split()))
arr1 = []
max_val = arr[0]
min_val = arr[0]

for i in arr[1:]:
    if min_val > i:
        min_val = i

cnt = arr.index(min_val)

for k in arr[cnt:]:
    arr1.append(k)

print(max(arr1)-min_val)
    
    