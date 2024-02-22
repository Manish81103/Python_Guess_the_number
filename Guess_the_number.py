import random
randNumber=random.randint(1,100)
print("<<<< Guess The Number Between 1 To 100 >>>>")
#print(randNumber)

userGuess=None
guesses = 0


while(userGuess!=randNumber):
     userGuess=int(input("Enter Your Guess:"))
     guesses+=1
     if(userGuess==randNumber):
         print("<<<<< You Guessed It Right! >>>>>")
     else:
         if(userGuess>randNumber):
            print("<<<< You Guessed It Wrong! Enter A Smaller Number >>>>")    
         else:
             print("<<<< You Guessed It Wrong! Enter A Larger Number >>>>")    

print(f"You guesses the number in {guesses} gusses")