n = int(input())
arr = list(map(float, input().split()))

sum_val = sum(arr)
avg_val = sum_val / n

print(f"{avg_val:.1f}")

if avg_val < 3.0:
    print("Poor")
elif avg_val < 4.0:
    print("Good")
else:
    print("Perfect")


