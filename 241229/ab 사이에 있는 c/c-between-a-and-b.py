a, b, c = map(int, input().split())

for i in range(a, b+1):
    if i % c == 0:
        satis = True
if satis == True:
    print("YES")
else:
    print("NO")