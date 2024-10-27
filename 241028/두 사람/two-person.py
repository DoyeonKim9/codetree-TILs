arr1 = input().split()
a1 = int(arr1[0])
b1 = str(arr1[1])
arr2 = input().split()
a2 = int(arr2[0])
b2 = str(arr2[1])

if (a1 >= 19 or a2 >= 19) and (b1 == 'M' or b2 == 'M'):
    print("1")
else:
    print("0")