c = 1
d = 2
e = 3
f = 4
def change(a, b):
    flag = a
    a = b
    b = flag
    print(a, b)


change(c, d)
print(c, d)
change(e, f)
change(d, e)

print(c, d, e, f)