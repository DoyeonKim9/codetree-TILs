n = int(input())
arr = list(map(int, input().split()))
min_minus = 100

for i in range(n):
    for j in range(i+1, n):
        minus = arr[j] - arr[i]

        if minus < min_minus:
            min_minus = minus
print(min_minus)
    