n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    mul_val = 1
    for j in range(a, b+1):
        mul_val *= j
    print(mul_val)
        
