import random

print('\n')
print("Ayy buddy let's roll some dice right?")

run = True

while(run == True):


    print('\n')
    # input number of sides
    sides = input("How Many Sides? ")
    while(sides.isdigit() == False):
        sides = input("Please enter a number. ")
    sides = int(sides)
    print("OK %i sides," % (sides), end='')

    # input number of dice
    valdice = False
    while(valdice == False):
        dice = input(" how many dice? (1-32) ")
        while(dice.isdigit() == False):
            dice = input("Please enter a number. ")
        dice = int(dice)
        if(dice > 0 and dice <= 32):
            valdice = True
        else:
            print("Sorry", end='')
            continue

    # Run and display results
    print
    print("%i d%i rolled as..." % (dice, sides))
    while(dice > 0):
        print(random.randrange(1,(sides+1)), ' ', end='')
        dice -= 1
    print('\n')
    print('\n')

    # continue or end
    runin = " "
    while(runin != "y" and runin != "Y" and runin != "n" and runin != "N"):
        runin = input("Continue? (y/n) ")
        if(runin == "n" or runin == "N"):
            run = False
# end operation
print("\n", "Thanks for rolling with me, homie.")