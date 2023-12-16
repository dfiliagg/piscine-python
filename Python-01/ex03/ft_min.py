import sys

def my_min(z=0, x=0, y=0):
    res = z
    if x >= y <= z:
        res = y
    elif y >= x <= z:
        res = x
    return res

def main():
    try:
        if len(sys.argv) != 4:
            raise Exception()
        print("The min is:", my_min(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])))
    except:
        print("Error! Usage: python3 ft_min.py <x> <y> <z>")


if __name__ == "__main__":
    main()

