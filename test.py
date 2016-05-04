#Biggest
def Big(Numbers):
	Num = raw_input("Number: ")

	if Num == "":
		out = """The highest number is {}""".format(Numbers)
		print out
	else:
		if Numbers > float(Num):
			Big(Numbers)
		else:
			Big(float(Num))





Big(-float("inf"))

def small(Numbers):
	Num = raw_input("Number:")
	if Num == "":
		out = """The highest number is {}""".format(Numbers)
		print out
	else:
		if Numbers > float(Num):
			Big(Numbers)
		else:
			Big(float(Num))
	out = """The smaller number is {}""".format(Num)
	print out


def pow(x,n):
	if n == 0: 
		return 1
	else: 
		return x * pow(x,n-1)


def main():
	print pow(8,3)	
main()

