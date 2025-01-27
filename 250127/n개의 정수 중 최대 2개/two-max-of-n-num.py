import sys
n = int(input())
arr = list(map(int, input().split()))
max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

arr.remove(max_val)

max_val2 = arr[0]

for j in arr:
    if j > max_val2:
        max_val2 = j

print(max_val, max_val2)


