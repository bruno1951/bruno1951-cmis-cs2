def first(x):
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
	total = 0 
	if x > 0:
		while x > 0:
			if x % 2 == 1:
				total += x

			x -= 1
	elif x < 0:	
		while x < 0:
			if x % 2 == 1:
				total += x
			x += 1
	
	return total
	
	
		

def grid(w, h):
	out = ""
	while h > 0:
		h = w
		while w > 0:
			out += "."
			w -= 1
		out += "\n"
		h -= 1
	return out

		
	




def main():

	print sumofOdds(6)
	print grid(60, 20)

main()


