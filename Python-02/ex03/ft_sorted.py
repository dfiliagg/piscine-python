import sys

if len(sys.argv) < 3:
    print("Error! You must insert at least 2 numbers")
    exit()
i = 1
ok = True
list = []
while i < len(sys.argv) -1:
    list.append(int(sys.argv[i]))
    if sys.argv[i] < sys.argv[i+1]:
        ok = False
    i += 1
if ok:
    print("The inserted sequence is sorted!")
    exit()
list.append(int(sys.argv[i]))
print("The inserted sequence is not sorted!")
print("The correct order is", sorted(list, reverse = True))