n = int(input())
sum_val = 0
ans = -1


for i in range(1, 101, 1):
    sum_val += i
    if sum_val >= n:
        ans = i
        break
    
    
print(ans)