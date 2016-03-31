
def main():


	out = """Type in 3 numbers""" 
	print out

	number1 = raw_input("A:")

	number2 = raw_input("B:")

	number3 = raw_input("C:")

	if (number2 > number1) and (number2 > number3): 
		biggest = number1
	
	elif (number1 > number2) and (number1 > number3): 
		biggest = number2
	
	else:
		biggest = number3


	output = """The largest number was {}""".format(biggest)
	print output

main()
