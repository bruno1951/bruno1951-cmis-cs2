def function3(a, b):
	if b <= 0:
		return a
	else:
		return a + b + function3(a, b - 1)

def function4(a, b, c):
	if a > b and a > c:
		return 1 + function4(b+1, c , a)
	elif b > a or b > c:
		return 1 - function4(b-1, c, a)
	else: 
		return  a+b+c

def main():
	c1 = function3(-2,3)
	c2 = function3(4, -2)
	c3 = function3(5,5)
	print c1
	print c2
	print c3
	d1 = function4(1,2,3)
	d2 = function4(3,2,1)
	d3 = function4(1,3,2)
	print d1
	print d2
	print d3
	
main()
