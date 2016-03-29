import math


def numberofducks(v):
	volume = 0.5 * v 


def howtofind(a, b, c):
	return int((a * b ) / c)

def output (a, b, c, d):
	out = """ So we have been noticing the decreasing number of ducks lately, and we want to make sure that it is really true. We might have to start importing ducks so then this habitat won't start changing. Area 1 have reported to have at least {} ducks, and area 2 has {} ducks. We took a little walk and fortunetly managed to count {} ducks. 
. 
""". format(a, b, c)
	return output

def main():
	
	a1= int(raw_input("The number of ducks in area 1 : "))
	
	a2= int(raw_input("The number of ducks in area 2: "))
	
	a3= int(raw_input("The number of ducks the environmentalists managed to to count while walking around : "))

	Ducky = howtofind(a1, a2, a3)

	if int(Ducky) < 5:
		print  "We will need to start importing some ducks in, as our residual is ",str(Ducky)

	elif int(Ducky) > 5:
		print "We will not need to start importing in some ducks, as our residual is " ,str(Ducky)
	


main()
