try:
	h = int(input("Insert hours: "))
	m = int(input("Insert minutes: "))
	s = int(input("Insert seconds: "))
	print ("Total seconds:", h * 3600 + m * 60 + s)
except:
	print ("Error: Invalid input.")