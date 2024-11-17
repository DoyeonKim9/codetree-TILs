n = int(input())
i = int
for i in range(1, n+1):
    if n // i > 1:
        n = n // i
        continue
    if n // i <= 1:
        print(i)
        break
