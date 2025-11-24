import random
getnum=int(input("Enter 1 for stone , 2 for :paper  , 3 for sessior ::"))
yourdict={1:"stone",2:"Paper",3:"Sessior"}
computerchoice=random.choice([1,2,3])
computerdict={1:"stone",2:"Paper",3:"Sessior"}
print("Your choice is :",yourdict[getnum])
print("Computer choice is :",computerdict[computerchoice])

if(computerchoice==getnum):
    print("Its a draw ):")
 
else:
    if(computerchoice==1 and getnum==2):
        print("You Win Paper beats Stone .")
    elif(computerchoice==1 and getnum==3):
        print("You Lose Stone smash sessior .")
    elif(computerchoice==2 and getnum==1):
        print("You Lose Paper covers stone .")
    elif(computerchoice==2 and getnum==3):
        print("You Win Paper cuts stone .")
    elif(computerchoice==3 and getnum==1):
        print("You Win Stone smash sessior")
    elif(computerchoice==3 and getnum==2):
        print("You lose Sessior cuts Paper .")
    else:
        print("You Entered Wrong Choice ")