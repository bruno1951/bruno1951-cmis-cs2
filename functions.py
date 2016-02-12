def add(a, b): #creating formula so then the cpu can add
	return a+b

def sub(a, b): #creating formula so then the cpu can sub
	return a-b 

def mul(a,b): #creating formula so then the cpu can multiply
	return a*b

def div(a,b): #creating formula so then the cpu can divide
	return a/b 

def hours_from_seconds(a): #creating formula so then the cpu can find the number of seconds in an hour
	return a/3600 
print hours_from_seconds(86400)

import math 

def circle_area(a):
	return math.pi * (a**2)

print circle_area(5)


def sphere_volume(a):
	return 1.33333333333 * math.pi * (a**3) 

print sphere_volume(5)

def avg_volume(a,b):
	c= a/2
	d= b/2
	y = (1.33333333333 * math.pi *c*c*c) 
 	x =(1.33333333333 * math.pi *d*d*d)
	return (y + x) /2


print avg_volume(10,20) 


def area(a,b,c) :
	
	s= (a+b+c) / 2 
	return (s*(s - a) * (s - b) * (s - c)) ** 0.5
 
print area(1,2,2.5)

def right_align(a):
	
	return (80-len(a))*(" ") + a
print right_align( "Hello" )  



	
def center (a):
	
	return (40-len(a))*(" ") + a
print center("Hallo") 

def msg_box (a)
	
	

 


	

