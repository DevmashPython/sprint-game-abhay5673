import msvcrt
import time

finish=10
count=0

print "  enter d to move right "
print " enter s to move down "
print "press enter key to start the game!"

raw_input()
s_time=time.time()

def turn_right():
	count=0
	while(1):
			code=msvcrt.getch()
			if code=='d':
				count=count+1
				print "--",
				if count==finish:
					print "dumbo u hav to move down"
					turn_down()
					break
			else:
				print "u lost the game! goodbye"
				break
	return
def turn_down():
	count=0
	while(1):
			code=msvcrt.getch()
			if code=='s':
					count=count+1
					print "\t\t\t\t|"
					if count==finish:
						print "haha nice u gotta move right now",
						
						break
			else:
					print "goodbye u lost "
					break
	return
					

turn_right()
count=0
while(1):
		code=msvcrt.getch()
		if code=='d':
				count=count+1
				print "--",
				if count==finish:
						print "game ended"
						break
		else:
			print "ur a loser"
			break
time_elapsed=time.time()-s_time
print "time elapsed,"+str(time_elapsed)





