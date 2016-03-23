import random

def absyourdifference(firstNo, secondNo):
	return abs(firstNo - secondNo)
	
def main(): 
	minimum = raw_input("Type in the minimum number:")
	maximum = raw_input("Type in the maximum number:")

	output = """I'm thinking of a number between {} and {} """.format(minimum, maximum)
	print output


	number = random.randint(int(minimum), int(maximum))
	your_number = raw_input("Guess the number:")

	
	output = """The number was {}.
Your guess was {}.
""".format(number,your_number)
	print output
	
	if int(your_number) == int(number):
		print  "Congratulations, You have guessed the number correctly"

	elif int(your_number) > int(number):
		print "Your guess was over by" ,str(absyourdifference(int(your_number), int(number)))
	
	elif int(your_number) < int(number) :
		print "Your guess was under by" ,str(absyourdifference(int(your_number), int(number)))



main()








#What is the minimum number? 5
#What is the maximum number? 10
#I'm thinking of a number from 5 to 10.
#What do you think it is?: 7
#The target was 9.
#Your guess was 7.
#That's under by 2.




