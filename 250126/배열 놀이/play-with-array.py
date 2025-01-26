n, q = map(int, input().split())

arr_n = list(map(int, input().split()))

for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        print(arr_n[a[1]-1])
    elif a[0] == 2:
        for j in range(n):
            if arr_n[j] == a[1]:
                print(j+1)
                break
        else:
            print("0")
    elif a[0] == 3:
        for j in range(a[1] - 1, a[2]):
            print(arr_n[j], end = " ")
        print()
