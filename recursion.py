def adder(num, total):
 	num = raw_input("The next number:")
	if num == "":
		out = """The running total is: {}""".format(total)
		print out
		return total
	else:
		total += float(num) 
		num = raw_input("Running total: " + str(total) + "\nNext number: ")
	
	
	return adder(num, total)
	
	
adder(0,0)



def bigger 
	
