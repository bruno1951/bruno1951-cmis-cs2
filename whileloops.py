x = 10
while x <= 0:
	print x
	x -= 1




def whiles(x):

	while x > 0:
		print x
		x -= 1
		


def counter(x):
	while x < 0:
		print x 
		x += 1

	while x > 0:
		print x 
		x -= 1


def addup(x): 
	pass

def countFrom2(x,y):	
	while x < y:
		print x
		x += 1
	while x > y:
		print x 
		x -= 1

def sumofOdds(x): 
	while x < 0:
		print x
		x += 1
	

	while x > 1:
		print x
		x -= 1
	
		


def main():
	whiles(10)
	counter(15)
	countFrom2(63, 43)
	sumofOdds(54)
main()


