c = 1
d = 2
e = 3
f = 4
def change(a, b):
    return b, a

print(c, d, e, f)

c,d = change(c, d)
e,f = change(e, f)
d,e = change(d, e)

print(c, d, e, f)