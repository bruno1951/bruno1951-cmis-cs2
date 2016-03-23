import math
import random

a = raw_input("Type in the number of ducks ")
b = raw_input("Type in the number of ducks you managed to count ")

print "We have noticed the population of wild ducks to be decreasing in zone a. However, we cannot be certain of this yet. The observed number of ducks we counted last week was " + str(a) + ". Please go count them. And report the number to us. Seems like you managed to count " + str(b) +  " Now lets put this to the test"

def subtract(a, b):
	return a-b 
