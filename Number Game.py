import random

print("Lets play a game to guess a number between 1 to 100")
# x = int(random.randint(1,100))
x = 56
flag = False
count = 1
while (flag==False):
    num = int(input("Guess your number "+str(count)))
    if (num>x):
        print("Your number is greater than the required number")
    elif(num<x):
        print("Your number is smaller than the required number")
    else:
        if (count==1):
            print("You guessed the right answer which is "+str(num)+" in "+str(count)+" try.")
        else:
            print("You guessed the right answer which is " + str(num) + " in " + str(count) + " tries.")
        flag=True
    count+=1
