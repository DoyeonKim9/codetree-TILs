arr = list(map(int, input().split()))

odd = arr[::2]
even = arr[1::2]

sum_val1 = sum(odd)
sum_val2 = sum(even)

if sum_val1 > sum_val2:
    print(sum_val1 - sum_val2)
else:
    print(sum_val2 - sum_val1)
