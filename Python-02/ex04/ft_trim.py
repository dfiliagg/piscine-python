import sys

def trim(list):
    del list[len(list)-1]
    del list[0]
    return None

def main():
    if len(sys.argv) < 3:
        print("Error! You must insert at least 2 values")
        exit()
    del sys.argv[0]
    trim(sys.argv)
    print("The new list is:", sys.argv)

if __name__ == "__main__":
    main()
