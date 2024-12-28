a, b, c = map(int, input().split())
satis = True

for i in range(a, b+1):
    if i % c == 0:
        satis = False
if satis == True:
    print("YES")
else:
    print("NO")