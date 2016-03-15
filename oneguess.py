import random

def main(): 
	minimum = raw_input("Type in the minimum number")
	maximum = raw_input("Type in the maximum number")

	output = """ I'm thinking of a number between {} and {} """.format(minimum, maximum)
	print output


	number = random.randint(minimum, maximum)
	your_number = raw_input("What do you think was the number?")




	



main()




#What is the minimum number? 5
#What is the maximum number? 10
#I'm thinking of a number from 5 to 10.
#What do you think it is?: 7

#The target was 9.
#Your guess was 7.
#That's under by 2.




