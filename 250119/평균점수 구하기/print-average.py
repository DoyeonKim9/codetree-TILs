arr = list(map(float, input().split()))
cnt = len(arr)
sum_val = sum(arr)
avg = sum_val / cnt
print(f"{avg:.1f}")