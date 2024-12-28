n = int(input())
satis = True

for i in range(2, n):
    if n % i == 0:
        satis = False
if satis == True:
    print("P")
else:
    print("C")