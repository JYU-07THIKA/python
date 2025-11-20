import random

computer = random.choice([-1,0,1])
youstr=input("enter your choice: ")
youdict={"s":1,"p":-1 , "sc":0}
reversedict={1:"stone",-1:"paper",0:"scissors"}

you = youdict[youstr]

print(f"you choose {reversedict[you]}\n computer choose {reversedict[computer]}")

if computer == you:
    print("its a draw")
else:
    if computer ==-1 and you == 0: 
        print("you win")
    elif computer == -1 and you ==1:
        print("you loose")
    elif computer ==1 and you == 0:
        print("you loose")
    elif computer == 1 and you ==-1:
        print("you win")
    elif computer ==0 and you == -1:
        print("you loose")
    elif computer == 0 and you == 1:
        print("you win")
    else:
        print("something went wrong")

