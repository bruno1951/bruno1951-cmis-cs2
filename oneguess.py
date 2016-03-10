import random

def random_number
minimum = raw_input("Type in the mininum number")
maximum = raw_input("Type in the maximum number")



#What is the minimum number? 5
#What is the maximum number? 10
#I'm thinking of a number from 5 to 10.
#What do you think it is?: 7

#The target was 9.
#Your guess was 7.
#That's under by 2.



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


