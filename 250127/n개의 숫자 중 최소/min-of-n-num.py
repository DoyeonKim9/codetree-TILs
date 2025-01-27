import sys
n = int(input())
arr = list(map(int, input().split()))

min_val = sys.maxsize
for i in arr:
    if min_val > i:
        min_val = i

print(f"{min_val} {arr.count(min_val)}")