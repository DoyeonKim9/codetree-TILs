n = int(input())
arr = list(map(int, input().split()))
max_val = 0

for i in range(n):
    for j in range(i+1, n):
        val = arr[j] - arr[i]

        if val > max_val:
            max_val = val
print(max_val)
# 따로따로의 최댓값 최솟값을 변수로 두고 계산하는 것이 아닌 문제의 조건인 최대 이익 즉,
# 값들의 차잇값의 최댓값을 구하는 것을 변수로 둬서 계산하기
    
    