import random,time
from playsound import playsound


def board(xstate,zstate):
	a= 'X' if xstate[0]==1 else ('O' if zstate[0]==1 else 0 )
	b= 'X' if xstate[1]==1 else ('O' if zstate[1]==1 else 1 )
	c= 'X' if xstate[2]==1 else ('O' if zstate[2]==1 else 2 )
	d= 'X' if xstate[3]==1 else ('O' if zstate[3]==1 else 3 )
	e= 'X' if xstate[4]==1 else ('O' if zstate[4]==1 else 4 )
	f= 'X' if xstate[5]==1 else ('O' if zstate[5]==1 else 5 )
	g= 'X' if xstate[6]==1 else ('O' if zstate[6]==1 else 6 )
	h= 'X' if xstate[7]==1 else ('O' if zstate[7]==1 else 7 )
	i= 'X' if xstate[8]==1 else ('O' if zstate[8]==1 else 8 )
	print("",a,"|",b,"|",c)
	print("---|---|---")
	print("",d,"|",e,"|",f)
	print("---|---|---")
	print("",g,"|",h,"|",i)

def xtrun(xvalue,xstate,rc,zstate):
	xstate[xvalue]=1
	rc.remove(xvalue)
	board(xstate,zstate)

def wincheck(xstate,zstate,win):
	for w in range(len(win)):
		if xstate[win[w][0]]+xstate[win[w][1]]+xstate[win[w][2]] ==3:
			winpoint=1
			return winpoint
		elif zstate[win[w][0]]+zstate[win[w][1]]+zstate[win[w][2]] ==3:
			winpoint=2
			return winpoint
		else:
			continue;

def computer_enter(xstate,zstate,win,rc,i):
	en=0
	if i>0:
		for ze in win:
			en=en+1
			if zstate[ze[0]]+zstate[ze[1]]==2:                  # winning ai
				if zstate[ze[0]]+zstate[ze[1]]+xstate[ze[2]]==2:
					zvalue=ze[2]
					return zvalue
			if 	zstate[ze[1]]+zstate[ze[2]]==2:
				if zstate[ze[1]]+zstate[ze[2]]+xstate[ze[0]]==2:
					zvalue=ze[0]
					return zvalue
			if zstate[ze[2]]+zstate[ze[0]]==2:
				if zstate[ze[2]]+zstate[ze[0]]+xstate[ze[1]]==2:
					zvalue=ze[1]
					return zvalue
		for xe in win:
			en=en+1		
			if xstate[xe[0]]+xstate[xe[1]]==2:                  # trep ai
				if xstate[xe[0]]+xstate[xe[1]]+zstate[xe[2]]==2:
					zvalue=xe[2]
					return zvalue
			if 	xstate[xe[1]]+xstate[xe[2]]==2:
				if xstate[xe[1]]+xstate[xe[2]]+zstate[xe[0]]==2:
					zvalue=xe[0]
					return zvalue
			if xstate[xe[2]]+xstate[xe[0]]==2:
				if xstate[xe[2]]+xstate[xe[0]]+zstate[xe[1]]==2:
					zvalue=xe[1]
					return zvalue
	if en==16:
		zvalue=random.choice(rc)
		return zvalue

print(' WELCOME To')
time.sleep(0.5)
title=['Tic', 'Tac', 'Toe']
for a in range(0,3):
	print("___",title[a],"___")
	time.sleep(0.5)
while True:
	print('')
	playsound("C:\\Users\\UJJWAL\\Music\\WIN_sound_effect_no_copyright(128k).mp3")
	turn=1
	win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	xstate=[0,0,0,0,0,0,0,0,0]
	zstate=[0,0,0,0,0,0,0,0,0]
	rc=[0,1,2,3,4,5,6,7,8]
	time.sleep(0.5)
	board(xstate,zstate)
	time.sleep(0.5)
	player=input('''
		1 for One player
		2 for Two player
		  EXIT    			
		    -''')


	if player=="1":

		i=0
		while len(rc)>0 :
			if turn==1:
				print("Your Chance")
				xvalue=int(input("Enter the value :"))
				if xstate[xvalue]==0 and zstate[xvalue]==0:
					xtrun(xvalue,xstate,rc,zstate)
					turn=0
					i = i+1
				else:
					print("Enter only remaining value")
			elif turn==0:
				time.sleep(1.5)
				print("computer Chance")
				zvalue=computer_enter(xstate,zstate,win,rc,i)
				print("Computer Enter =",zvalue)
				if xstate[zvalue]==0 and zstate[zvalue]==0:
					zstate[zvalue]=1
					turn=turn+1
					i = i+1
					rc.remove(zvalue)
					board(xstate,zstate)

				else:
					print("Enter only remaining value")
			else:
				print("error")

			if i>=5:
				winpoint=wincheck(xstate,zstate,win)
				if winpoint==1:
					print("____X is winner____")
					playsound("C:\\Users\\UJJWAL\\Music\\Audience_Clapping_-_Sound_Effect(128k).mp3")
					break;
				if winpoint==2:
					print("____O is winner____")
					playsound("C:\\Users\\UJJWAL\\Music\\Audience_Clapping_-_Sound_Effect(128k).mp3")
					break;
				else:
					continue;
			else:
				continue;


	elif player=="2":
		i=0
		while len(rc)>0 :
			if turn==1:
				print("1st Player Chance")
				xvalue=int(input("Enter the value :"))
				if xstate[xvalue]==0 and zstate[xvalue]==0:
					xtrun(xvalue,xstate,rc,zstate)
					i=i+1
					turn=0
				else:
					print("Enter only remaining value")
			elif turn==0:	
				print("2nd Player Chance")
				zvalue=int(input("Enter the value :"))
				if xstate[zvalue]==0 and zstate[zvalue]==0:
					zstate[zvalue]=1
					turn= turn + 1
					i=i+1
					rc.remove(zvalue)
					board(xstate,zstate)
				else:
					print("Enter only remaining value")
			else:
				print("error")

			if i>=5:
				winpoint=wincheck(xstate,zstate,win)
				if winpoint==1:
					print("____X is winner____")
					playsound("C:\\Users\\UJJWAL\\Music\\Audience_Clapping_-_Sound_Effect(128k).mp3")
					break;
				if winpoint==2:
					print("____O is winner____")
					playsound("C:\\Users\\UJJWAL\\Music\\Audience_Clapping_-_Sound_Effect(128k).mp3")
					break;
				else:
					continue;
			else:
				continue;




	else: 
		s=input("you are sure for exit y/n :")
		if s=="y" or s=="Y":
			exit()
		else:
			pass;
	print("repeat")	