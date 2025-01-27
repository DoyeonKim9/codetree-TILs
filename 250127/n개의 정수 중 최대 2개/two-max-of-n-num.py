# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

# Step 1: 처음 2개의 원소 중 더 큰 값을 max1에
#                        더 작은 값을 max2에 넣습니다.
if arr[0] > arr[1]:
    max1, max2 = arr[0], arr[1]
else:
    max2, max1 = arr[0], arr[1]

# Step 2: 3번째 원소부터 보면서 max1과 max2를 갱신합니다.
for i in range(2, n):
    if arr[i] >= max1:
        # Case 1 : 지금까지 본 숫자들보다 좋다면
        #          max2, max1 모두 갱신해줍니다.
        max2, max1 = max1, arr[i]
    elif arr[i] > max2:
        # Case 2 : max2보다만 좋다면 max2를 갱신합니다.
        max2 = arr[i]

print(max1, max2)
