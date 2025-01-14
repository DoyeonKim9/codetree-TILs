n = int(input())
cnt = 'A'
for i in range(n):
    for j in range(i):
        print(" ", end =" ")
    for j in range(n-i, 0, -1):
        print(cnt, end = " ")
        cnt = chr(ord(cnt) + 1)
    print()
