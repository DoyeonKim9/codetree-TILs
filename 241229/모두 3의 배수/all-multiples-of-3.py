satis = True
for i in range(1, 6):
    a = int(input())
    if a % 3 != 0:
        satis == False
if satis == True:
    print("1")
else:
    print("0")
    