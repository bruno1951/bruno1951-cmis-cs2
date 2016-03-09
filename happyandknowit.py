
def clapYourHands():
    print "clap clap"

def stompYourFeet():
    print "stomp stomp"

def main():
	youreHappy = raw_input (""" Are you happy, type True or False """) == "True"
	youKnowIt = raw_input (""" IF you know it, type True or False  """) == "True" 

	if youreHappy and youKnowIt: #boolean expression 
		clapYourHands()
		stompYourFeet()

	print "Good bye"
main()

x = 26
y = 25
z = 0

if x < y :
	print "Okay"
	print "Yes"
	z = x + y
print "Done"
print z






import random 

def wrestle(playerStrength, enemyStrength, playerAttackValue):
    
	targetValue = random.random()

	playerAttackResult = playerStrength + abs(playerAttackValue - targetValue)    

	enemyAttackResult =  enemyStrength + targetValue
 
	if playerAttackResult > enemyAttackResult:
		return True
	else:
        	return False

print wrestle(0 , 0 ,0 )



