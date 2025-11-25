# f=open("test.txt","r")
# tesx=f.read()
# print(tesx)



'''Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.'''

# f=open("poems.txt","r")
# readtext=f.read()
# print(readtext)
# f.seek(0)
# new=f.readline()
# print(new)
# f.seek(0)
# print(f.readlines())
# f.seek(0)
# readtext.lower()
# if "twinkle" in readtext :
#     print("Yes")
# count=readtext.count("twinkle")
# print(count)




'''The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘test.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score'''

import random
def change():
    with open("test.txt","r") as f:
         currscore=f.read()
    print("Previous High score is ",currscore)
    # f.seek(0)
    newscore=int(currscore.split("=")[1].strip())
#   f.close()
    newscore +=1
    with open("test.txt","w") as f:
       f.write(f"highscore={newscore}")
    f=open("test.txt")
    newhighscore=f.read()
    print("New high score is ",newhighscore)
    f.close()

def game ():
    
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
             change()
         elif(computerchoice==1 and getnum==3):
             print("You Lose Stone smash sessior .")
         elif(computerchoice==2 and getnum==1):
             print("You Lose Paper covers stone .")
         elif(computerchoice==2 and getnum==3):
             print("You Win Paper cuts stone .")
             change()
         elif(computerchoice==3 and getnum==1):
             print("You Win Stone smash sessior")
             change()
         elif(computerchoice==3 and getnum==2):
             print("You lose Sessior cuts Paper .")
         else:
            print("You Entered Wrong Choice ")
game ()