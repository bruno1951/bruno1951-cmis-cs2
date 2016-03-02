#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# It is a assignment operator, used to put a value into a variable
# 
#
#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements or formulas that will perform a computation 
#
#
#3 1pt) What does the keyword "return" do?
# It is a principle in program that takes some input (doesn't matter how many) and return outs with a output 
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: float
#	2: string
#	3: Tuple 
#	4: int
#	5: len
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function call is an expression that contains a simple name along with parenthesized argument list, this list can contain any number of expressions that are separated by commas. 
# 
# A function definition how ever defines the function instead to provide the required functionality, all it does is give it a name, specifies the parameters. 
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Code
#	2: Processing 
#	3: Output?
#
#Part 2: Programming (25 points)




#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi


import math 

def diameter(c1, c2 ,c3) :
	return 2 * (c1**0.5 )/ math.pi
	return 2 * (c2**0.5 )/ math.pi
	return 2 * (c3**0.5 )/ math.pi

def output( a, b, c, total):
	output = """

Diameter 
c1 {}
c2 {}
c3 {}
Total {}

""". format(a, b, c, total)
	return out
def main():
	a= raw_input("Type in an area:")
	b= raw_input("Type in an area:")
	c= raw_input("Type in an area:")
	c1 = diameter(a)
	c2 = diameter(b)
	c3 = diameter(c) 
	add = c1 + c2 + c3 

out = output(a , b, c, total)
print output

main()





