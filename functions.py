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


import math 

def circle_area(a): #defining the process that is required to find an normal area of a circle
	return math.pi * (a**2)




def sphere_volume(a): # Defining the equations that is required to to find out the volume of a sphere
	return 1.33333333333 * math.pi * (a**3) 



def avg_volume(a,b): #this will help find the average volume of those two areas 
	c= a/2
	d= b/2
	y = (1.33333333333 * math.pi *c*c*c) 
 	x =(1.33333333333 * math.pi *d*d*d)
	return (y + x) /2





def area(a,b,c) : # This will help find the area of this triangle 
	
	s= (a+b+c) / 2 
	return (s*(s - a) * (s - b) * (s - c)) ** 0.5
 


def right_align(a): # this will right align the message 
	
	return (80-len(a))*(" ") + a




	
def center (a): # This will centralize the message in the middle 
	
	return (40-len(a))*(" ") + a



def msg_box(a): #This will 
	return "+" + ((len(a)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (a)+ (2*" ") + "|" + "\n" + "+" + ((len(a)+4)*"-") + "+"  


 
 
add1 = add (5, 1) 
add2 = add(7, 6)
 
sub1 = sub(4,4)
sub2 = sub(9,5)

mul1 = (6, 5)
mul2 = (8, 2)

div1 = (5,6)
div2 = (6,7)

hours_from_seconds1 = (21,600)
hours_from_seconds2 = (32400)

circle_area1 = (4)
circle_area2 = (6)

sphere_volume1 = (7)
sphere_volume2 = (8)

avg_volume1 = (15, 25) 
avg_volume2 = (35, 80)

area1 = (2, 3 , 3.5) 
area2 = (5, 6, 6.5)

right_align1 = ("Herro")
right_align2 = (" This is hard ")

center1 = ("This better be centralized")
center2 = (" Bomin is old for her grade")

msg_box1 = (" Steven smells " )
msg_box2 = (" My partners are meanys" )


print msg_box(str(add1))
