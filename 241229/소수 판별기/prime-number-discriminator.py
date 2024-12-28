n = int(input())
satis = True

for i in range(1, n):
    if n % i == 0:
        satis = False
if satis == True:
    print("C")
else:
    print("P")