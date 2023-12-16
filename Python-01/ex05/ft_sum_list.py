def sum_list(list):
    res = 0
    for element in list:
        res += int(element)
    return res

def main():
    list = []
    n = int(input("Insert integer: "))
    while n != 0:
        list.append(n)
        n = int(input("Insert integer: "))
    print("The sum is:", sum_list(list))

if __name__ == "__main__":
    main()
