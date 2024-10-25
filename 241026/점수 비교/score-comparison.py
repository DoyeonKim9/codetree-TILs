arr1 = input().split()
m1 = int(arr1[0])
e1 = int(arr1[1])

arr2 = input().split()
m2 = int(arr2[0])
e2 = int(arr2[1])

if m1 > m2 and e1 > e2:
    print("1")
else:
    print("0")