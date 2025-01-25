n = int(input())
arr = list(map(int, input().split()))
arr_cnt = [0] * 9
for i in arr:
    arr_cnt[i-1] += 1

for j in arr_cnt:
    print(j)
