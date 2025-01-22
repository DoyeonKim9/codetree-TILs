arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    if i == 0:
        break
    arr1.append(i)
cnt = 0
sum_val = 0
for j in arr1:
    if j % 2 == 0:
        cnt += 1
        sum_val += j

print(f"{cnt} {sum_val}")
    