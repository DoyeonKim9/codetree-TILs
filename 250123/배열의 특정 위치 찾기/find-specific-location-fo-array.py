arr = list(map(int, input().split()))
arr1 = arr[1::2]
arr2 = arr[2::3]
sum_val = sum(arr1)
avg = sum(arr2) / len(arr2)
print(f"{sum_val} {avg:.1f}")

