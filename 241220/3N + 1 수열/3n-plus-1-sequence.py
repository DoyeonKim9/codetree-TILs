n = int(input())
cnt = 0
while True:
    if n % 2 == 0:
        n = n // 2
        cnt += 1
    elif n == 1:
        break
    else:
        n = n * 3 + 1
        cnt += 1
print(cnt)