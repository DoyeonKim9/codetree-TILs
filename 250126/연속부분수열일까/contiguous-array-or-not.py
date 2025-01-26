n1, n2 = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

ans = False
for i in range(len(arr_a)-len(arr_b)+1):
    if arr_a[i:i+len(arr_b)] == arr_b:
        ans = True
if ans == True:
    print("Yes")
else:
    print("No")