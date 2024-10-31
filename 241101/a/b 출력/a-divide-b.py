a, b = map(int, input().split())
n = a // b
print(f"{n}.", end = "")
a %= b
for i in range(20):
    a *= 10
    print(a // b, end="")
    a %= b