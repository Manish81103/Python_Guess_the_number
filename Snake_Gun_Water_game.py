import random

def gamewin(computer,you):
    if computer==you:
        return None
    elif computer=="snake":
        if you=="water":
            return False
        elif you=="gun":
            return True
    elif computer=="water":
        if you=="gun":
            return False
        elif you=="snake":
            return True
    elif computer=="gun":
        if you=="snake":
            return False
        elif you=="water":
            return True 

print("Computer Turn:\n Choose any one: snake / water / gun? ") 
randNo=random.randint(1,3)

if randNo==1:
    computer="snake"
elif randNo==2:
    computer="water"   
elif randNo==3:
    computer="gun"
you=input("Your Turn:\n Choose any one: snake / water / gun? ")    
a=gamewin(computer,you)


print(f"Computer choose: {computer}")
print(f"You choose: {you}")

if a== None:
    print("The game is a tie!")
elif a:
     print("You Won!")
else:   
     print("You Lost!")  

