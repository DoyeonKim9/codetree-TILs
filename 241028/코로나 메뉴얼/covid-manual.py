arr1 = input().split()
cold1 = str(arr1[0])
sym1 = int(arr1[1])

arr2 = input().split()
cold2 = str(arr2[0])
sym2 = int(arr2[1])

arr3 = input().split()
cold3 = str(arr3[0])
sym3 = int(arr3[1])

count = 0

if cold1 == "Y" and sym1 >= 37:
    count += 1
if cold2 == "Y" and sym2 >= 37:
    count += 1
if cold3 == "Y" and sym3 >= 37:
    count += 1
if count >= 2:
    print("E")
else:
    print("N")