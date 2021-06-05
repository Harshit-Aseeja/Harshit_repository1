#from random import randint
#num=randint(0,100)
#intro
print("WELCOME TO THE GUESSING GAME!\n\n\nHERE ARE THE RULES:\n1)A number is generated at random by the system\n2)you have to try and guess that number\n3)if the number you guess is within a range of 10 integers to the generated number the system will say WARM else it will say COLD\n4)if your next guess is more accurate than your previous one the system will say WARMER else it will say COLDER\n\nENJOY!\n")

from random import randint
num= randint(0,100)
#print(num)
guess_list=[]
guess=0
x=0

while x!=num:
  x=int(input("enter your guess:  "))
  guess_list.append(x)
  guess+=1
  last_guess=guess_list[guess-2]
  
  
  if guess<=1:
    if(num==x):
      print("YOU GOT IT IN FIRST GO BABY") 

    elif (num-10<x<num+10):
      print("WARM!")
    
    else:
      print("COLD!")
  elif guess>1:
    
    if(num==x):
      print("WOOHOO! you got it, you took {} guesses".format(guess))
    
    elif(abs(num-last_guess) > abs(num-x) ):
      print("WARMER")
    
    else:
      print("COLDER")
