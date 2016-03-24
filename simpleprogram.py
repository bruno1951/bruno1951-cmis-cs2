import math
import random



def subtract(this, that):
	return this - that 




def main():
	a = raw_input ("Type in the number of ducks ")
	b = raw_input ("Type in the number of ducks you managed to count ")

	print "We have noticed the population of wild ducks to be decreasing in zone a. However, we cannot be certain of this yet. The observed number of ducks we counted last week was " + str(a) + ". Please go count them. And report the number to us. Seems like you managed to count " + str(b) +  " Now lets put this to the test"
	lastyear =  raw_input("Type in the number of ducks for last year, it should be higher than 20 ")
	if lastyear < 20:
			lastyear = random.randint(20,100)
	migrated = raw_input("Type in the number of ducks that migrated ")


	this_year = subtract(int(a,b)
	ducks_rgone = this_year * last_year / migrated
	
	if int(ducks_rgone) > 10:
		print  "We believe that the ducks are decreasing in this zone"

	elif int(ducks_rgone) < 10:
		print "The ducks are not decreasing in this zone, and are just hidden somewhere else" 
	
	
main()
	
