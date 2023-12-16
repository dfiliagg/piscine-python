import sys

i = 0
for val in sys.argv:
    i+=1
if i != 3:
    print("Error: insert only 2 number")
    exit()
try:
	num1 = float(sys.argv[1])
	num2 = float(sys.argv[2])
except ValueError:
	print("ERROR: Please enter two numbers.")
	exit()
if num1 > num2:
	print(num1, "is greater than", num2)
elif num1 < num2:
	print(num1, "is less than", num2)
else:
	print(num1, "is equal to", num2)
