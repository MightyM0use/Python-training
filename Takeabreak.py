import time #import the time library
import webbrowser #import the webbrowser library


total_breaks = 3 #the loop must repeat three times
break_count = 0 #initialize the meter with zero

print("This program started on" +time.ctime()) #tells us when the program start (on current time)
while (break_count < total_breaks) : #if the break count is inferior to total breaks then continue the loop
	time.sleep (10) #tell the program to stay quiet for that time
	webbrowser.open ("https://www.youtube.com/watch?v=naW6-WxmMiU") #tell the program to open a video in the webbrowser when time's up
	break_count = break_count + 1 #add one iteration to the loop until 3
	