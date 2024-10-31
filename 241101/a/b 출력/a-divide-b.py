a, b = map(int, input().split())
n = a / b
div1 = a % b * 10
div2 = div1 % b
print(n, end = "")
for i in range(19):
    print(div2, end = "")