string = input("Insert a string: ")
if len(string) > 20:
	print(string[len(string)-20:])
elif len(string) < 20:
	print(" " * (20 - len(string)) + string)
else:
	print(string)