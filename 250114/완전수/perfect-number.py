start, end = map(int, input().split())
rcnt = 0
for i in range(start, end + 1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += j
    if cnt == i:
        rcnt += 1  
print(rcnt)
        
        


