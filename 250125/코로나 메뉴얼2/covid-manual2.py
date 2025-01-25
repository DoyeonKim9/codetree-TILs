cnt = [0] * 4

for i in range(3):
    a, b = input().split()
    b = int(b)
    if a == 'Y' and b >= 37:
        cnt[0] += 1
    elif a == 'N' and b >= 37:
        cnt[1] += 1
    elif a == 'Y' and b < 37:
        cnt[2] += 1
    elif a == 'N' and  b < 37:
        cnt[3] += 1
for j in cnt:
    print(j, end = " ")
if cnt[0] >= 2:
    print("E")
