# Simple Output Colour helper
# Author : Matt Lorentzen
# Made as an import 

#!/usr/bin/python

def redtxt(text2colour):
	redstart = "\033[0;31m"
	redend = "\033[0m"
	return redstart + text2colour + redend

def greentxt(text2colour):
	greenstart = "\033[0;32m"
	greenend = "\033[0m"
	return greenstart + text2colour + greenend
	
def yellowtxt(text2colour):
	yellowstart = "\033[0;33m"
	yellowend = "\033[0m"
	return yellowstart + text2colour + yellowend
	
def bluetxt(text2colour):
	bluestart = "\033[0;34m"
	blueend = "\033[0m"
	return bluestart + text2colour + blueend


""" Following code loop will show all the colours
for num in range(30,50): #and (90,100)
	print "Num code is : " + str(num)
	talk = ("\033[0;" + str(num) + "mHello\033[0m")
	print talk
	time.sleep(0.5)
"""
