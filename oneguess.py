import random

def main(): 
	minimum = raw_input("Type in the minimum number:")
	maximum = raw_input("Type in the maximum number:")

	output = """ I'm thinking of a number between {} and {} """.format(minimum, maximum)
	print output


	number = random.randint(int(minimum), int(maximum))
	your_number = raw_input("Guess the number:")
	output = """ The number was {} """.format(number)
	print output	
	output = """ Your guess was {} """.format(your_number) 	
	


	if your_number > number:
		difference = int(your_number) -  int(number)
		output = """ Your guess was {} higher """.format(difference)
		print output	
	
	elif your number < number:
		more_than = int(number) - int(number)
		output = """ Your guess was {} lower """.format(more_than)
		print output 

	else: your_number == number:
		output = """ Congratulations, you guessed the number correctly """		
		print output		
	



main()








#What is the minimum number? 5
#What is the maximum number? 10
#I'm thinking of a number from 5 to 10.
#What do you think it is?: 7
#The target was 9.
#Your guess was 7.
#That's under by 2.




