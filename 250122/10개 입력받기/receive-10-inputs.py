arr = list(map(int, input().split()))
arr1 = []
for i in arr:
    if i == 0:
        break
    arr1.append(i)
sum_val = sum(arr1)
avg = sum_val / len(arr1)

print(f"{sum_val} {avg:.1f}")