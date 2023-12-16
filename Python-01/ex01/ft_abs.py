exp = input("Insert an expression: ")
try:
    res = eval(exp)
    if res < 0:
        res *= -1
    print("The result is:", float(res))
except:
    print("Error: insert a valid expression")
