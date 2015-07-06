#!/usr/bin/python
# Testing colours file

import colours

print colours.redtxt("This is me printing in Red")

print colours.greentxt("This is me printing in Green")

for num in range(5):
	num = colours.bluetxt(str(num))
	print "This is me printing %s inside the loop as a pre-coloured variable" %num
	
print "This is me chaining the colours with nesting :" + colours.redtxt("This is a Red block with a " + colours.yellowtxt("Yellow ") + "block inside.") 
