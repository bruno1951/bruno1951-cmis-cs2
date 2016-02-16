def add(a, b): #creating formula so then the cpu can add
	return a+b
print add(3, 4)
def sub(a, b): #creating formula so then the cpu can sub
	return a-b
print add(5, 3) 

def mul(a,b): #creating formula so then the cpu can multiply
	return a*b
print mul(4,4)

def div(a,b): #creating formula so then the cpu can divide
	return a/b 
print div(2, 3)
def hours_from_seconds(a): #creating formula so then the cpu can find the number of seconds in an hour
	return a/3600 
print hours_from_seconds(86400)

import math 

def circle_area(a): #defining the process that is required to find an normal area of a circle
	return math.pi * (a**2)

print circle_area(5)


def sphere_volume(a): # Defining the equations that is required to to find out the volume of a sphere
	return 1.33333333333 * math.pi * (a**3) 

print sphere_volume(5)

def avg_volume(a,b): #this will help find the average volume of those two areas 
	c= a/2
	d= b/2
	y = (1.33333333333 * math.pi *c*c*c) 
 	x =(1.33333333333 * math.pi *d*d*d)
	return (y + x) /2


print avg_volume(10,20) 


def area(a,b,c) : # This will help find the area of this triangle 
	
	s= (a+b+c) / 2 
	return (s*(s - a) * (s - b) * (s - c)) ** 0.5
 
print area(1,2,2.5)

def right_align(a): # this will right align the message 
	
	return (80-len(a))*(" ") + a
print right_align( "Hello" )  



	
def center (a): # This will centralize the message in the middle 
	
	return (40-len(a))*(" ") + a
print center("Hallo") 


def msg_box(a): #This will 
	return "+" + ((len(a)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (a)+ (2*" ") + "|" + "\n" + "+" + ((len(a)+4)*"-") + "+"  
print msg_box("Hello")
print msg_box(" I finally got this done " ) 
 


print add(3, 4)
print add(5, 3) 
print mul(4,4)
print div(2, 3)
print hours_from_seconds(86400)
print circle_area(5)
print sphere_volume(5)
print avg_volume(10,20) 
print area(1,2,2.5)
print right_align( "Hello" )  
print center("Hallo") 
print msg_box("Hello")
print msg_box(" I finally got this done " ) 
 
first = add(3, 4) 
second = add(5, 3) 
third = mul(4,4)
fourth = div(2, 3)
fifth = hours_from_seconds(86400)
sixth = circle_area(5)
seventh = sphere_volume(5)
eighth = avg_volume(10,20) 
ninth = area(1,2,2.5)
tenth = right_align( "Hello" )  
eleven = center("Hallo") 
twelve = msg_box("Hello")
thirdteen = msg_box(" I finally got this done " ) 
 
thewholething = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth + eleven + twelve + thirdteen
print thewholething
