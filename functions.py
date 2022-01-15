import random
from array import *
import config


# This function generate a random number (would roll a dice) in order to get the ability scores
def rollDice():

    numArray = array('i', [])

    for i in range(4):
        num = random.randint(1, 6)
        numArray.append(num)

    numArray = sorted(numArray)
    highest_sum = numArray[1] + numArray[2] + numArray[3]
    return highest_sum


# This is the function defines the different races and converts the user input to the race
def raceTranslation():

    if config.temp_r == 1:
        config.race = "Dragonborn"
        config.temp_str2 = 2
        config.temp_dex2 = 0
        config.temp_const2 = 0
        config.temp_wis2 = 0
        config.temp_intelli2 = 0
        config.temp_charisma2 = 1

    elif config.temp_r == 2:
        config.race = "Dwarf"
        config.temp_str2 = 0
        config.temp_dex2 = 0
        config.temp_const2 = 2
        config.temp_wis2 = 0
        config.temp_intelli2 = 0
        config.temp_charisma2 = 0

    elif config.temp_r == 3:
        config.race = "Elf"
        config.temp_str2 = 0
        config.temp_dex2 = 2
        config.temp_const2 = 0
        config.temp_wis2 = 0
        config.temp_intelli2 = 0
        config.temp_charisma2 = 0

    elif config.temp_r == 4:
        config.race = "Gnome"
        config.temp_str2 = 0
        config.temp_dex2 = 0
        config.temp_const2 = 0
        config.temp_wis2 = 0
        config.temp_intelli2 = 2
        config.temp_charisma2 = 0

    elif config.temp_r == 5:
        config.race = "Half-Elf"
        config.temp_str2 = 0
        config.temp_dex2 = 0
        config.temp_const2 = 0
        config.temp_wis2 = 0
        config.temp_intelli2 = 0
        config.temp_charisma2 = 2

        for i in range(2):
            print("Because you've chosen Half-Elf, you can increase 2 ability scores by 1.\n 1 for Strength\n 2 for Dexterity\n 3 for Constitution\n 4 for Wisdom\n 5 for Intelligence\n")
            option = int(input("Type your answer: "))
            if option == 0:
                print("")
            elif option == 1:
                config.temp_str2 += 1
            elif option == 2:
                config.temp_dex2 += 1
            elif option == 3:
                config.temp_const2 += 1
            elif option == 4:
                config.temp_wis2 += 1
            elif option == 5:
                config.temp_intelli2 += 1
            else:
                print("Error: Something went wrong - 2")

    elif config.temp_r == 6:
        config.race = "Halfling"
        config.temp_str2 = 0
        config.temp_dex2 = 2
        config.temp_const2 = 0
        config.temp_wis2 = 0
        config.temp_intelli2 = 0
        config.temp_charisma2 = 0

    elif config.temp_r == 7:
        config.race = "Half-Orc"
        config.temp_str2 = 2
        config.temp_dex2 = 0
        config.temp_const2 = 1
        config.temp_wis2 = 0
        config.temp_intelli2 = 0
        config.temp_charisma2 = 0

    elif config.temp_r == 8:
        config.race = "Human"
        config.temp_str2 = 1
        config.temp_dex2 = 1
        config.temp_const2 = 1
        config.temp_wis2 = 1
        config.temp_intelli2 = 1
        config.temp_charisma2 = 1

    elif config.temp_r == 9:
        config.race = "Tiefling"
        config.temp_str2 = 0
        config.temp_dex2 = 0
        config.temp_const2 = 0
        config.temp_wis2 = 0
        config.temp_intelli2 = 1
        config.temp_charisma2 = 2

    else:
        print("Something went wrong.")


# This is the function defines the different classes and converts the user input to a class
def classTranslation():
    # The variable temp_c is the temporary value which helps determine the class
    # The variable cache is used to cache the bonus for the skills
    global cache

    global AnimalHandling
    global Athletics
    global Acrobatics
    global SleightOfHand
    global Stealth
    global Arcana
    global History
    global Investigation
    global Intimidation
    global Nature
    global Religion
    global Perception
    global Survival
    global Insight
    global Medicine
    global Deception
    global Performance
    global Persuasion

    if config.temp_c == 1:
        config.Class = "Barbarian"
        for i in range(2):
            print("Because you've chosen Barbarian, you gain Proficency two of these skills.\n 1 for Animal Handling\n 2 for Athletics\n 3 for Intimidation\n 4 for Nature\n 5 for Perception\n 6 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 0:
                print("Option is 0")
            elif option == 1:
                config.AnimalHandling += cache
            elif option == 2:
                config.Athletics += cache
            elif option == 3:
                config.Intimidation += cache
            elif option == 4:
                config.Nature += cache
            elif option == 5:
                config.Perception += cache
            elif option == 6:
                config.Survival += cache
            else:
                print("Error: Something went wrong")

    elif config.temp_c == 2:
        config.Class = "Bard"
        for i in range(3):
               print("Because you've chosen Bard, You gain proficency in three skills of your choice. \n 1 for Athletics\n 2 for Acrobatics\n 3 for Sleight of Hand\n 4 for Stealth\n 5 for Arcana\n 6 for History\n 7 for Investigation\n 8 for Nature\n 9 for Religion\n 10 for Animal Handling\n 11 for Insight\n 12 for Medicine\n 13 for Perception\n 14 for Survival\n 15 for Deception\n 16 for Intimidation\n 17 for Performance\n 18 for Persuasion\n")
               option = int(input("Type your answer: "))
               if option == 1:
                   config.Athletics += cache
               elif option == 2:
                   config.Acrobatics += cache
               elif option == 3:
                    config.SleightOfHand += cache
               elif option == 4:
                   config.Stealth += cache
               elif option == 5:
                   config.Arcana += cache
               elif option == 6:
                   config.History += cache
               elif option == 7:
                   config.Investigation += cache
               elif option == 8:
                   config.Nature += cache
               elif option == 9:
                   config.Religion += cache
               elif option == 10:
                   config.AnimalHandling += cache
               elif option == 11:
                   config.Insight += cache
               elif option == 12:
                   config.Medicine += cache
               elif option == 13:
                   config.Perception += cache
               elif option == 14:
                   config.Survival += cache
               elif option == 15:
                   config.Deception += cache
               elif option == 16:
                   config.Intimidation += cache
               elif option == 17:
                   config.Performance += cache
               elif option == 18:
                   config.Persuasion += cache
               else:
                   print("Error: Somethng went wrong")

    elif config.temp_c == 3:
        config.Class = "Cleric"
        for i in range(2):
            #edit the line below
            print("Because you've chosen Cleric, you gain proficency in two of these skills.\n 1 for History\n 2 for Insight\n 3 for Medicine\n 4 for Persuasion\n 5 for Religion\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.History += cache
            elif option == 2:
                config.Insight += cache
            elif option == 3:
                config.Medicine += cache
            elif option == 4:
                config.Persuasion += cache
            elif option == 5:
                config.Religion += cache
            else:
                print("Error: Something went wrong")
    elif config.temp_c == 4:
        config.Class = "Druid"
        for i in range(2):
            #edit the line below
            print("Because you've chosen Druid, you gain proficency in two of these skills.\n 1 for Arcana\n 2 for Animal Handling\n 3 for Insight\n 4 for Medicine\n 5 for Nature\n 6 for Perception\n 7 for Religion\n 8 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Arcana += cache
            elif option == 2:
                config.AnimalHandling += cache
            elif option == 3:
                config.Insight += cache
            elif option == 4:
                config.Medicine += cache
            elif option == 5:
                config.Nature += cache
            elif option == 6:
                config.Perception += cache
            elif option == 7:
                config.Religion += cache
            elif option == 8:
                config.Survival += cache
            else:
                print("Error: Something went wrong")

    elif config.temp_c == 5:
            config.Class = "Fighter"
            #not finished
            print("Because you've chosen Fighter, you gain proficeny in two of these skills.\n 1 for Acrobatics\n 2 for Animal Handling\n 3 for Athletics\n 4 for History\n 5 for Insight\n 6 for Intimidation\n 7 for Perception\n 8 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Arcana += cache
            elif option == 2:
                config.AnimalHandling += cache
            elif option == 3:
                config.Insight += cache
            elif option == 4:
                config.Medicine += cache
            elif option == 5:
                config.Nature += cache
            elif option == 6:
                config.Perception += cache
            elif option == 7:
                config.Religion += cache
            elif option == 8:
                config.Survival += cache
            else:
                print("Error: Something went wrong")

    elif config.temp_c == 6:
            config.Class = "Monk"
            #not finished
            print("Because you've chosen Druid, you can increase 2 ability scores by 1.\n 1 for Animal Handling\n 2 for Athletics\n 3 for Intimidation\n 4 for Nature\n 5 for Perception\n 6 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Arcana += cache
            elif option == 2:
                config.AnimalHandling += cache
            elif option == 3:
                config.Insight += cache
            elif option == 4:
                config.Medicine += cache
            elif option == 5:
                config.Nature += cache
            elif option == 6:
                config.Perception += cache
            elif option == 7:
                config.Religion += cache
            elif option == 8:
                config.Survival += cache
            else:
                print("Error: Something went wrong")

    elif config.temp_c == 7:
        config.Class = "Paladin"

    elif config.temp_c == 8:
        config.Class = "Ranger"

    elif config.temp_c == 9:
        config.Class = "Rogue"

    elif config.temp_c == 10:
        config.Class = "Sorcerer"

    elif config.temp_c == 11:
        config.Class = "Warlock"

    elif config.temp_c == 12:
        config.Class = "Wizard"
    else:
        print("Something went wrong.")


def LevelConversion():
    global cache

    if config.lvl == 1:
        cache = 2

    elif config.lvl == 2:
        cache = 2

    elif config.lvl == 3:
        cache = 2

    elif config.lvl == 4:
        cache = 2

    elif config.lvl == 5:
        cache = 3

    elif config.lvl == 6:
        cache = 3

    elif config.lvl == 7:
        cache = 3

    elif config.lvl == 8:
        cache = 3

    elif config.lvl == 9:
        cache = 4

    elif config.lvl == 10:
        cache = 4

    elif config.lvl == 11:
        cache = 4

    elif config.lvl == 12:
        cache = 4

    elif config.lvl == 13:
        cache = 5

    elif config.lvl == 14:
        cache = 5

    elif config.lvl == 15:
        cache = 5

    elif config.lvl == 16:
        cache = 5

    elif config.lvl == 17:
        cache = 6

    elif config.lvl == 18:
        cache = 6

    elif config.lvl == 19:
        cache = 6

    elif config.lvl == 20:
        cache = 6

    else:
        Error()


# This function defines what the program will do in case of an error or unexpected case
def Error():
    print("There was an unknown error. Please try again")
    quit()