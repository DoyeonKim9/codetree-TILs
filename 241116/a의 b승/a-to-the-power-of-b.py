a, b = map(int, input().split())
prod = 1
for _ in range(1, b+1):
    prod *= a
print(prod)