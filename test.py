import random 

def wrestle(playerStrength, enemyStrength, playerAttackValue):
    
	targetValue = random.random()

	playerAttackResult = playerStrength + abs(playerAttackValue - targetValue)    

	enemyAttackResult =  enemyStrength + targetValue
 
	if playerAttackResult > enemyAttackResult:
		return True
	else:
        	return False

print wrestle ( 1, 2, 3)



