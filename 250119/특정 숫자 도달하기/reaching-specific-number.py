arr = list(map(int, input().split()))

sum_val = 0
cnt = 0
for i in arr:
    if i < 250:
        sum_val += i
        cnt += 1
    if i > 250:
        break
avg_val = sum_val / cnt

print(f"{sum_val} {avg_val:.1f}")
