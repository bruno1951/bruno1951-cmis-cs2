def main():
	print """This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""
	get = float(0)
	number0 = raw_input("N0:")
	if float(number0) > 10 or float(number0) < 0:
		out = """ {} is out of range""".format(number0)
		print out
		number0 = 0.0
	else: float(number0) + get
	

	number1 = raw_input("N1:")
	if float(number1) > 10 or float(number1) < 0:
		out = """ {} is out of range""".format(number1)	
		print out
		number1 = 0.0
	else: float(number1) + get
	
	
	number2 = raw_input("N2:")
	if float(number2) > 10 or float(number2) < 0:
		out = """ {} is out of range""".format(number2)	
		print out
		number2 = 0.0
	else: float(number2) + get
	

	number3 = raw_input("N3:")
	if float(number3) > 10 or float(number3) < 0: 
		out = """ {} is out of range""".format(number3)	
		print out
		number3 = 0.0
	else: float(number3) + get
	


	number4 = raw_input("N4:")
	if float(number4) > 10 or float(number4) < 0:
			out = """ {} is out of range""".format(number4)
			print out
			number4 = 0.0 
	else: float(number4) + get

	
	
	avgthing = float(number0) + float(number1) + float(number2) + float(number3) + float(number4)
	

	
	avgdiv = [number0, number1, number2, number3, number4].count(get)

	
	divs = 5 - avgdiv

	avg = avgthing / divs
	intavg = int(avg)

	out1 = """The average number is {} """.format(avg)
	out2 = """The integer is {}""".format(intavg) 
	
	print out1
	print out2
		

	is_even = intavg % 2 == True
	if is_even == True:
		print "It is Odd"
	else: 
		print "It is even"
	


main()	


	 
 
	
