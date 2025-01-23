n = int(input())
arr = list(map(int, input().split()))

new = [(i*i) for i in arr]

for j in new:
    print(j, end =" ")