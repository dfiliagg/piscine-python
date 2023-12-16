import sys

def summo(n):
    res = 0
    while n != 0:
        res += n
        n -= 1
    return res

try:
    if len(sys.argv) != 2:
        raise Exception
    n = int(sys.argv[1])
    if int(sys.argv[1]) < 0:
        print("Error! n must be >=0")
        exit()
    print("The sum is:", summo(n))
except Exception:
    print("Error! Usage: python3 ft_summorial.py <n>")
