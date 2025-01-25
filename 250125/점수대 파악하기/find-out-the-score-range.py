arr = list(map(int, input().split()))
cnt = [0] * 11

for i in arr:
    cnt[i // 10] += 1
    if i == 0:
        break
for j in range(100, 9, -10):
    print(f"{j} - {cnt[j//10]}")