import random
import math

def weapon(item):

	if item == "wooden sword":
		strength = 15    
		speed = 100

	elif item == " iron sword ":
		strength = 50 
		speed = 50

	elif item == "mace":
		strength = 25
		speed = 75
	
	elif item == "fists":
		strength = 5
		speed = 150

	elif item == " Battle ax ":
		strength = 150
		speed = 25

	elif item == "hunting Bow" :
		strength = 55
		speed = 45
		rangeofattack = 100
	elif item == "long bow"
   
	
def getAttackValue():

    number = int(raw_input("Type attack value (0-99): "))
    if number > 99 or number < 0:
        number = random.randint(0, 99)
    attackValue = float(number)/100
    return attackValue    


def wrestle(playerStrength, enemyStrength, playerAttackValue):

    targetValue = random.random()
    playerAttackResult = playerStrength + abs(playerAttackValue - targetValue)    
    enemyAttackResult =  enemyStrength + targetValue
    if playerAttackResult > enemyAttackResult:
        return True
    else:
        return False


def resultTemplate(playerStrength, enemyStrength, result):

    if result == True:
        msg = "wins"
    else:
        msg = "loses"
    return """
Player strength: {}
Enemy strength: {}
Player {}!
""".format(playerStrength, enemyStrength, msg)


def main():


    playerFood = raw_input("What do you want to eat? ")
    enemy1Food = raw_input("What does enemy 1 eat? ")
    enemy2Food = raw_input("What does enemy 2 eat? ")

    playerStrength = eat(playerFood)
    enemy1Strength = eat(enemy1Food)
    enemy2Strength = eat(enemy2Food)

    playerAttackValue1 = getAttackValue()
    result1 = wrestle(playerStrength, enemy1Strength, playerAttackValue1)

    playerAttackValue2 = getAttackValue()   
    result2 = wrestle(playerStrength, enemy2Strength, playerAttackValue2)
    
    output = """
You ate {}.
Enemy 1 ate {}.
Enemy 2 ate {}.
""".format(playerFood, enemy1Food, enemy2Food)
    output += resultTemplate(playerStrength, enemy1Strength, result1)
    output += resultTemplate(playerStrength, enemy2Strength, result2)

    print output
main()
