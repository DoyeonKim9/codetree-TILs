while True:
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    c = str(arr[2])

    if c != 'C':
        print(a*b)
        continue
    
    else:
        print(a*b)
        break

