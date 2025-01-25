arr = list(map(int, input().split()))
cnt = [0] * 10
for i in arr:
    cnt[i] += 1

for j in range(1, 7):
    print(f"{j} - {cnt[j]}")
