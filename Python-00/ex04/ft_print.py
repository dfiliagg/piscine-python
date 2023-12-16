string = input("Insert a string: ")
try:
	n = int(input("Insert an integer: "))
	if 0 <= n < len(string):
		print(string[n:-n+1])
	else:
		print("Error: index out of range")
except:
	print("Error: Invalid input.")	