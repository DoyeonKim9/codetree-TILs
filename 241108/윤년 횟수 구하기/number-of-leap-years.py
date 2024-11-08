n = int(input())
cnt_y = 0
for i in range(1, n+1):
    if i % 400 != 0 and i % 100 == 0:
        cnt_y -= 1
    if i % 4 == 0:
        cnt_y += 1
print(cnt_y)