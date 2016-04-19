def main():
	print """This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""

	number0 = raw_input("N0:")
	if float(number0) > 10 or float(number0) < 0:
		out = """ {} is out of range""".format(number0)	
		print out

	number1 = raw_input("N1:")
	if float(number1) > 10 or float(number1) < 0:
		out = """ {} is out of range""".format(number1)	
		print out
	number2 = raw_input("N2:")
	if float(number2) > 10 or float(number2) < 0:
		out = """ {} is out of range""".format(number2)	
		print out
	number3 = raw_input("N3:")
	if float(number3) > 10 or float(number3) < 0: 
		out = """ {} is out of range""".format(number3)	
		print out
	number4 = raw_input("N4:")
	if float(number4) > 10 or float(number4)< 0:
		out = """ {} is out of range""".format(number4)
		print out
	
main()	


	 

	
