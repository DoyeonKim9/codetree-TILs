n = int(input())

arr = list(map(int, input().split()))

new = [(i) for i in arr if i % 2 == 0]

for j in new:
    print(j, end = " ")