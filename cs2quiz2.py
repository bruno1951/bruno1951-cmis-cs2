#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) if 
#b) and
#c) else
#
#2) What does 'return' do?
# describes what will the def will do, and it will show what will be done to the input that will be given later
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) indentation allows the computer to know what is describing what, for example the return will be descrbing the def
#b) prevents an syntax error
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a)
#problem1_b) square root of -3 which is -9
#problem1_c)0
#problem1_d) -5
#
#problem2_a) true
#problem2_b) true
#problem2_c) false or syntax error
#problem2_d) false or syntax error 
#
#problem3_a) return c
#problem3_b) return b
#problem3_c) return a
#problem3_d) return b
#
#problem4_a)7
#problem4_b)5
#problem4_c)1.5
#problem4_d)5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)



def main():
	out = """Type in 3 numbers""" 
	print out

	number1 = raw_input("A:")
	number2 = raw_input("B:")
	number3 = raw_input("C:")
	
	if (number1 > number2) and (number1 > number3):
		biggest = number1
	
	elif (number2 > number1) and (number2 > number3): 
		biggest = number2
	
	else:
		biggest = number3


	output = """The largest number was {}""".format(biggest)
	print output





main()
