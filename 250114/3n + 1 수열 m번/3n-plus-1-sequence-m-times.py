n = int(input())


for i in range(n):
    a = int(input())
    cnt = 0
    while a != 1:
        if a % 2 == 0:
            a //= 2
        else:
            a = a * 3 + 1
        cnt += 1
    print(cnt)
    
