import sys
try:
    if len(sys.argv) != 4:
        raise Exception ()
    x, y, z = sys.argv[1:4]
    res = float(z)
    if float(y) <= float(x) >= float(z):
        res = x
    if float(z) <= float(y) >= float(x):
        res = y
    print("The max is:", float(res))
except:
    print("Error! Usage: python3 ft_max.py <x> <y> <z>")
