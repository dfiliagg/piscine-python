string = input("Insert a string: ")
try:
	n = int(input("insert an integer: "))
	if 0 <= n < len(string):
		print(string[n], string[-n])
	else:
		print("Error: index out of range")
except:
	print("Error: Invalid input.")