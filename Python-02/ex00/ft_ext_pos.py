import sys

try:
    if len(sys.argv) == 1:
        raise Exception
    pMax, pMin, i = 0, 0, 0
    min = None
    max = None
    for arg in sys.argv[1:]:
        arg = int(arg)
        if max == None or min == None:
            max, min, i = arg, arg, 1
            continue
        if max < arg:
            max, pMax = arg, i
        if min > arg:
            min, pMin = arg, i
        i += 1
    print("The min is", min,"and its position is", pMin)
    print("The max is", max, "and its position is", pMax)
except:            
    print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
