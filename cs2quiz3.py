

#Section 1: Terminology
# 1) What is a recursive function?
# A recursive function is a function that you can continue forever, and repeats itself until something else has been done. Calls itself
#
#
# 2) What happens if there is no base case defined in a recursive function?
# Then the function will not work, and will not end, and will just take in a input but doesn't really do anything with it
#
#
# 3) What is the first thing to consider when designing a recursive function?
# Create the base case
#
#
# 4) How do we put data into a function call?
# raw input, or use main()
#
# 
# 5) How do we get data out of a function call?
# base case
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 3,6 -1
#a2 = 7,2  -1
#a3 =-1 -1

#b1 = 2 +1
#b2 = 2,1 -1 
#b3 = 0,5 -1

#c1 = -1,3 -1 
#c2 = 4 +1 
#c3 = 15,14 -1

#d1 = 6 +1
#d2 =4,2,4    -1 
#d3 = 1,1,0     -1

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.




def main():
 	num = raw_input("The next number:")
	starter = float(0) 
	if num == "":
		out = """The average of your odd numbers is: """.format(total)
		print out
		return total
	else:
		if float(num) % 2 == True:
			num = 0 
		
		
		else: 
			total += float(num) 
			num = raw_input("Running total: " + str(total) + "\nNext number: ")
		



	
main()
