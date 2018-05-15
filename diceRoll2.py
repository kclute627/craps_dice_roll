

def dice_roll():
    import random
    '''roll 2 dice and try to equal 7 or 11.. if 7 or 11 is not reached prior to the user
     hitting their original number they lose and
    and the program tells them so .. if they hit 7 or 11 prior to hitting their point they win'''

    # introduction

    print(""" Hello and welcome to dice roll The objest of the game is to roll a 7 or 11 on you first roll \n or hit the number from your first roll\n\n\n""")
    # create y/n statment to see if user would like to play

    first_roll = random.randint(1, 6)
    second_roll = random.randint(1, 6)
    first_total = first_roll + second_roll

    print("The result of your first roll was {} and the result of your second roll was {} totaling {} \n\n".format(first_roll, second_roll, first_total))

    # what happens when you roll 7 or 11 on the first roll
    if first_total == 7 or first_total == 11:
        print("Congrulations you Won!!!!")

    # enter break of some sort to ask user if the would like to continue
    else:
        print("Your point is equal to {} that is not 7 or 11 so you must roll again good luck!!!! You must now roll a total of {}. If you hit a 7 or 11 before your point you will lose".format(first_total, first_total))

        print("Here we go lets try to hit that point of {}".format(first_total))

        while first_total != 7 or first_total != 11:

            # Continue to roll attemptint to hit your point
            first_roll1 = random.randint(1, 6)
            second_roll1 = random.randint(1, 6)
            second_total = first_roll1 + second_roll1

            print("Dice one is {} and dice two is {} when we add both dice up it totals {}".format(first_roll1, second_roll1, second_total))

            if first_total == second_total:
                print("Congrulations you rolled {} before rolling a 7 or 11".format(first_total))
                break
            elif second_total == 7 or second_total == 11:
                print("Bummer you lost try again")
                break


dice_roll()
