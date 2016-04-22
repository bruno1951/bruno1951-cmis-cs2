def adder(stuff, total):
    if stuff == "":
        return total
    else:
        total += float(stuff) 
        stuff = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder(stuff, total)

adder()
