# n = 5
# m = 1
# r = 0.16
# k = 0.11
# H = F = 1200
# pv = 0
# for i in range(n*m):
#     pv += (((H*k)/m)/((1+r/m)**i))

# pv += F/(1 + r)
# print(pv)

lst = [[142, 112], [25, 115, 550, 720, 125], [40]]
proc = [0.2, 0.25, 0.3]
for prc in proc:
    c = 0
    for l in range(len(lst)):
        s = 0
        for n in range(len(lst[l])):
            s += lst[l][n]/(1+prc)**(n+1)
        print(f"PV{l} {prc*100}% = {s}")
        c += s
    print(c + 40)
