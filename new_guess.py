import random

def rounds(theround, points):
	if theround == 0:
		out = """You got a score of {}""".format(points)
		print out 
	else:
		out = """Round {}""".format(theround)
		print out


		points += eachguess(random.randint(1, 100), 5)



		return rounds(theround -1, points)

def eachguess(randomized, trials):
	guess = raw_input("Guess a number:")
	if  guess == "":
		exit()

	elif int(guess) == randomized:
		print "Your guess was correct"




	elif trials == 1:
		print "You lose."
		return 0



	elif int(guess) > randomized:
		print "Your guess was too high."
		return eachguess(randomized, trials -1)
	

	elif int(guess) < randomized:
		print "Your guess was too low."
		return eachguess(randomized, trials -1)
	



def main():
	print rounds(10, 0)

main()
