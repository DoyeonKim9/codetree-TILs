a, b = map(int, input().split())
c = 0
cnt = [0] * 10
for i in range(a):
    c = a // b
    cnt[a % b] += 1
    a = c
    if c <= 1:
        break
    

sum_val = 0
for j in cnt:
    sum_val += j * j

print(sum_val)



