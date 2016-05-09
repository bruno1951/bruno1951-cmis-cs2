import random
import math

def weapon(item):

	if item == "wooden sword":
		strength = 15    
		speed = 100

	elif item == "iron sword ":
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

	else:
		strength = random.randomint(0, 60)
		speed = random.random(0, 60)
		print "Incorrect input, you have been penalized" 
	return strength 
	return speed
   
	
def character(person):

	if person == "Elf":
		strength = 50 
		speed = 70 


	if person == "Human":
		strength = 100
		speed = 50 

	
	if person == "Dwarf": 
		strength = 150
		speed = 40

	
	if person == "Orc": 	
		strength = 200
		speed = 20 

		 
	if person == "AUTOMAN":
		strength = 300
		speed = 400

	return strength 
	return speed

  


def hacknslash(playerStrength, playerspeed, enemystrength, enemyspeed):


	playerAttack = playerStrength 
	enemyAttackResult =  enemyStrength
	speed = playerspeed
	speed2 = enemyspeed
	enemyhealth = 200
	playerhealth = 200

	if speed > speed2:
		enemyhealth - playerAttack
		print "Succesful hit"
	elif speed2 > speed:
		playerhealth - enemyAttackResult  
		print "You've been hit" 
		
def fight(enemyhealth, playerhealth):
	
	if enemyhealth == 0 or enemyhealth < 0:
		out = """Enemy is down!"""
		print out
	elif enemyhealth > 0: 
		if speed > speed2
		enemyhealth - playerAttack
	elif playerhealth == 0 or playerhealth < 0:
		out = """You have been downed """
		print out
	elif playerhealth > 0: 
		hackslash()
	

def main():


	playerweapon = raw_input("Choose your weapon: ")
	playercharacter = raw_input("Choose your character: ")
	enemy_character = raw_input("Who will you be facing: ")	
	
	result = fight(playerhealth, enemyhealth)

main()
