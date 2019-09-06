
import sys, os, platform, pty, time, threading, glob
from random import *


timer1 = time.time()
timer1_old = time.time() 
current_temp = 0
last_temp = 0
rate = 0
refresh_rate = 2

def setRate(a=0):
	global rate 
	rate = a

def time_Since_Start():
	global timer1_old
	return time.time()-timer1_old

def temp_simulator():
	global current_temp
	global rate 
	global refresh_rate
	global timer1

	if (time.time() - timer1) >= (1/refresh_rate):
		current_temp = current_temp+((time.time() - timer1) * rate)
		timer1 = time.time()
	
	return current_temp



#setRate(2)


#while(1):
#	#print('{0:.2f} and {1:.2f} and'.format(time_Since_Start(),temp_simulator()))
#	print(f"> {time_Since_Start():.2f},{temp_simulator():.2f},{rate:.2f}")

#	time.sleep(.5) 

	

#	if current_temp >50:
#		setRate(1+random())
#		break
#	else:
#		setRate(2+random())


