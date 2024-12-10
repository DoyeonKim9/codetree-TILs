sum_val = 0
while True:
    n = int(input())
    if n % 2 == 1:
        continue
    print(n // 2)
    sum_val += 1

    if sum_val >=3:
        break
    
    
    