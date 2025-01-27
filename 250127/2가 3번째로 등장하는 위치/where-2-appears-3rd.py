n = int(input())
arr = list(map(int, input().split()))
cnt = 0
arr1 = []
for i in arr:
    arr1.append(i)
    if i == 2:
        cnt += 1
        if cnt == 3:
            break
print((len(arr1)))
