sum_val = 0
cnt = 0
while True:
    n = int(input())
    if n < 30:
        sum_val += n
        cnt += 1
        continue
    else:
        avg = sum_val / cnt
        print(f"{avg:.2f}")
        break
    
    

    