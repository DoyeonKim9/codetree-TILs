am, ae = map(int, input().split())
bm, be = map(int, input().split())

if am > bm or (am == bm and ae > be):
    print("A")
else:
    print("B")