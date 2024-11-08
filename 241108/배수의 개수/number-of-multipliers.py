cnt1 = 0
cnt2 = 0
for i in range(1, 11):
    n = int(input())
    if n % 3 == 0:
        cnt1 += 1
    if n % 5 == 0:
        cnt2 += 1
print(cnt1, end = " ")
print(cnt2)