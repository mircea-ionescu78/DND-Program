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
                print("Error: Something went wrong")
                Error()

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
        Error()


# This is the function defines the different classes and converts the user input to a class
def classTranslation():
    # The variable temp_c is the temporary value which helps determine the class
    # The variable cache is used to cache the bonus for the skills
    if config.temp_c == 1:
        config.Class = "Barbarian"
        for i in range(2):
            print("Because you've chosen Barbarian, you gain proficiency two of these skills.\n"
                  " 1 for Animal Handling\n 2 for Athletics\n 3 for Intimidation\n 4 for Nature\n 5 for Perception\n 6 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 0:
                print("Option is 0")
            elif option == 1:
                config.AnimalHandling += config.cache
            elif option == 2:
                config.Athletics += config.cache
            elif option == 3:
                config.Intimidation += config.cache
            elif option == 4:
                config.Nature += config.cache
            elif option == 5:
                config.Perception += config.cache
            elif option == 6:
                config.Survival += config.cache
            else:
                print("Error: Something went wrong")

    elif config.temp_c == 2:
        config.Class = "Bard"
        for i in range(3):
               print("Because you've chosen Bard, You gain proficiency in three skills of your choice. \n"
                     " 1 for Athletics\n 2 for Acrobatics\n 3 for Sleight of Hand\n 4 for Stealth\n"
                     " 5 for Arcana\n 6 for History\n 7 for Investigation\n 8 for Nature\n 9 for Religion\n"
                     " 10 for Animal Handling\n 11 for Insight\n 12 for Medicine\n 13 for Perception\n 14 for Survival\n"
                     " 15 for Deception\n 16 for Intimidation\n 17 for Performance\n 18 for Persuasion\n")
               option = int(input("Type your answer: "))
               if option == 1:
                   config.Athletics += config.cache
               elif option == 2:
                   config.Acrobatics += config.cache
               elif option == 3:
                    config.SleightOfHand += config.cache
               elif option == 4:
                   config.Stealth += config.cache
               elif option == 5:
                   config.Arcana += config.cache
               elif option == 6:
                   config.History += config.cache
               elif option == 7:
                   config.Investigation += config.cache
               elif option == 8:
                   config.Nature += config.cache
               elif option == 9:
                   config.Religion += config.cache
               elif option == 10:
                   config.AnimalHandling += config.cache
               elif option == 11:
                   config.Insight += config.cache
               elif option == 12:
                   config.Medicine += config.cache
               elif option == 13:
                   config.Perception += config.cache
               elif option == 14:
                   config.Survival += config.cache
               elif option == 15:
                   config.Deception += config.cache
               elif option == 16:
                   config.Intimidation += config.cache
               elif option == 17:
                   config.Performance += config.cache
               elif option == 18:
                   config.Persuasion += config.cache
               else:
                   print("Error: Somethng went wrong")
                   Error()

    elif config.temp_c == 3:
        config.Class = "Cleric"
        for i in range(2):
            print("Because you've chosen Cleric, you gain proficiency in two of these skills.\n"
                  " 1 for History\n 2 for Insight\n 3 for Medicine\n 4 for Persuasion\n 5 for Religion\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.History += config.cache
            elif option == 2:
                config.Insight += config.cache
            elif option == 3:
                config.Medicine += config.cache
            elif option == 4:
                config.Persuasion += config.cache
            elif option == 5:
                config.Religion += config.cache
            else:
                print("Error: Something went wrong")

    elif config.temp_c == 4:
        config.Class = "Druid"
        for i in range(2):
            print("Because you've chosen Druid, you gain proficiency in two of these skills.\n"
                  " 1 for Arcana\n"
                  " 2 for Animal Handling\n"
                  " 3 for Insight\n"
                  " 4 for Medicine\n"
                  " 5 for Nature\n"
                  " 6 for Perception\n"
                  " 7 for Religion\n"
                  " 8 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Arcana += config.cache
            elif option == 2:
                config.AnimalHandling += config.cache
            elif option == 3:
                config.Insight += config.cache
            elif option == 4:
                config.Medicine += config.cache
            elif option == 5:
                config.Nature += config.cache
            elif option == 6:
                config.Perception += config.cache
            elif option == 7:
                config.Religion += config.cache
            elif option == 8:
                config.Survival += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 5:
        config.Class = "Fighter"
        for i in range(2):
            print("Because you've chosen Fighter, you gain proficiency in two of these skills.\n"
                      " 1 for Acrobatics\n 2 for Animal Handling\n 3 for Athletics\n 4 for History\n"
                      " 5 for Insight\n 6 for Intimidation\n 7 for Perception\n 8 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Acrobatics += config.cache
            elif option == 2:
                config.AnimalHandling += config.cache
            elif option == 3:
                config.Athletics += config.cache
            elif option == 4:
                config.History += config.cache
            elif option == 5:
                config.Insight += config.cache
            elif option == 6:
                config.Intimidation += config.cache
            elif option == 7:
                config.Perception += config.cache
            elif option == 8:
                config.Survival += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 6:
        config.Class = "Monk"
        for i in range(2):
            print("Because you've chosen Druid, you can increase two ability scores by 1.\n"
                  " 1 for Animal Handling\n 2 for Athletics\n 3 for Intimidation\n"
                  " 4 for Nature\n 5 for Perception\n 6 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.AnimalHandling += config.cache
            elif option == 2:
                config.Athletics += config.cache
            elif option == 3:
                config.Intimidation += config.cache
            elif option == 4:
                config.Nature += config.cache
            elif option == 5:
                config.Perception += config.cache
            elif option == 6:
                config.Survival += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 7:
        config.Class = "Paladin"
        for i in range(2):
            print("Because you've chosen Paladin, you can increase two ability scores by 1.\n"
                  " 1 for Athletics\n 2 for Insight\n 3 for Intimidation\n"
                  " 4 for Medicine\n 5 for Persuasion\n 6 for Religion\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Athletics += config.cache
            elif option == 2:
                config.Insight += config.cache
            elif option == 3:
                config.Intimidation += config.cache
            elif option == 4:
                config.Medicine += config.cache
            elif option == 5:
                config.Persuasion += config.cache
            elif option == 6:
                config.Religion += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 8:
        config.Class = "Ranger"
        for i in range(3):
            print("Because you've chosen Ranger, you can increase three ability scores by 1.\n"
                  " 1 for Animal Handling\n 2 for Athletics\n 3 for Insight\n"
                  " 4 for Investigation\n 5 for Nature\n 6 for Perception\n 7 for Stealth\n 8 for Survival\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.AnimalHandling += config.cache
            elif option == 2:
                config.Athletics += config.cache
            elif option == 3:
                config.Insight += config.cache
            elif option == 4:
                config.Investigation += config.cache
            elif option == 5:
                config.Nature += config.cache
            elif option == 6:
                config.Perception += config.cache
            elif option == 7:
                config.Stealth += config.cache
            elif option == 8:
                config.Survival += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 9:
        config.Class = "Rogue"
        for i in range(4):
            print("Because you've chosen Rogue, you can increase four ability scores by 1.\n"
                  " 1 for Acrobatics\n 2 for Athletics\n 3 for Insight\n"
                  " 4 for Investigation\n 5 for Deception\n 6 for Intimidation\n 7 for Stealth\n 8 for Perception\n"
                  " 9 for Performance\n 10 for Persuasion\n  11 for Sleight of Hand\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Acrobatics += config.cache
            elif option == 2:
                config.Athletics += config.cache
            elif option == 3:
                config.Insight += config.cache
            elif option == 4:
                config.Investigation += config.cache
            elif option == 5:
                config.Deception += config.cache
            elif option == 6:
                config.Intimidation += config.cache
            elif option == 7:
                config.Stealth += config.cache
            elif option == 8:
                config.Perception += config.cache
            elif option == 9:
                config.Performance += config.cache
            elif option == 10:
                config.Persuasion += config.cache
            elif option == 11:
                config.SleightOfHand += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 10:
        config.Class = "Sorcerer"
        for i in range(2):
            print("Because you've chosen Sorcerer, you gain proficiency two of these skills.\n"
                  " 1 for Arcana\n 2 for Deception\n 3 for Insight\n"
                  " 4 for Intimidation\n 5 for Persuasion\n 6 for Religion\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Arcana += config.cache
            elif option == 2:
                config.Deception += config.cache
            elif option == 3:
                config.Insight += config.cache
            elif option == 4:
                config.Intimidation += config.cache
            elif option == 5:
                config.Persuasion += config.cache
            elif option == 6:
                config.Religion += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 11:
        config.Class = "Warlock"
        for i in range(2):
            print("Because you've chosen Warlock, you gain proficiency two of these skills.\n"
                  " 1 for Arcana\n 2 for Deception\n 3 for History\n"
                  " 4 for Intimidation\n 5 for Investigation\n 6 for Nature\n 7 for Religion\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Arcana += config.cache
            elif option == 2:
                config.Deception += config.cache
            elif option == 3:
                config.History += config.cache
            elif option == 4:
                config.Intimidation += config.cache
            elif option == 5:
                config.Investigation += config.cache
            elif option == 6:
                config.Nature += config.cache
            elif option == 7:
                config.Religion += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    elif config.temp_c == 12:
        config.Class = "Wizard"
        for i in range(2):
            print("Because you've chosen Wizard, you gain proficiency two of these skills.\n"
                  " 1 for Arcana\n 2 for Insight\n 3 for History\n"
                  " 4 for Medicine\n 5 for Investigation\n 6 for Religion\n")
            option = int(input("Type your answer: "))
            if option == 1:
                config.Arcana += config.cache
            elif option == 2:
                config.Insight += config.cache
            elif option == 3:
                config.History += config.cache
            elif option == 4:
                config.Medicine += config.cache
            elif option == 5:
                config.Investigation += config.cache
            elif option == 6:
                config.Religion += config.cache
            else:
                print("Error: Something went wrong")
                Error()

    else:
        print("Something went wrong.")
        Error()


# This function converts the level into the ability points needed
def LevelConversion():

    if config.lvl == 1:
        config.cache = 2

    elif config.lvl == 2:
        config.cache = 2

    elif config.lvl == 3:
        config.cache = 2

    elif config.lvl == 4:
        config.cache = 2

    elif config.lvl == 5:
        config.cache = 3

    elif config.lvl == 6:
        config.cache = 3

    elif config.lvl == 7:
        config.cache = 3

    elif config.lvl == 8:
        config.cache = 3

    elif config.lvl == 9:
        config.cache = 4

    elif config.lvl == 10:
        config.cache = 4

    elif config.lvl == 11:
        config.cache = 4

    elif config.lvl == 12:
        config.cache = 4

    elif config.lvl == 13:
        config.cache = 5

    elif config.lvl == 14:
        config.cache = 5

    elif config.lvl == 15:
        config.cache = 5

    elif config.lvl == 16:
        config.cache = 5

    elif config.lvl == 17:
        config.cache = 6

    elif config.lvl == 18:
        config.cache = 6

    elif config.lvl == 19:
        config.cache = 6

    elif config.lvl == 20:
        config.cache = 6

    else:
        Error()


# This function converts the ability points into skill points for Strength
def StrengthConversion():

    if config.strength == 1:
        config.Athletics += -5
        config.strengthMod = -5

    elif config.strength == 2 or config.strength == 3:
        config.Athletics += -4
        config.strengthMod = -4

    elif config.strength == 4 or config.strength == 5:
        config.Athletics += -3
        config.strengthMod = -3

    elif config.strength == 6 or config.strength == 7:
        config.Athletics += -2
        config.strengthMod = -2

    elif config.strength == 8 or config.strength == 9:
        config.Athletics += -1
        config.strengthMod = -1

    elif config.strength == 10 or config.strength == 11:
        config.Athletics += 0
        config.strengthMod = 0

    elif config.strength == 12 or config.strength == 13:
        config.Athletics += 1
        config.strengthMod = 1

    elif config.strength == 14 or config.strength == 15:
        config.Athletics += 2
        config.strengthMod = 2

    elif config.strength == 16 or config.strength == 17:
        config.Athletics += 3
        config.strengthMod = 3

    elif config.strength == 18 or config.strength == 19:
        config.Athletics += 4
        config.strengthMod = 4

    elif config.strength >= 20:
        config.Athletics += 5
        config.strengthMod = 5

    else:
        Error()


# This function converts the ability points into skill points for Charisma
def CharismaConversion():

    if config.charisma == 1:
        config.Deception += -5
        config.Intimidation += -5
        config.Performance += -5
        config.Persuasion += -5
        config.charismaMod = -5

    elif config.charisma == 2 or config.charisma == 3:
        config.Deception += -4
        config.Intimidation += -4
        config.Performance += -4
        config.Persuasion += -4
        config.charismaMod = -4

    elif config.charisma == 4 or config.charisma == 5:
        config.Deception += -3
        config.Intimidation += -3
        config.Performance += -3
        config.Persuasion += -3
        config.charismaMod = -3

    elif config.charisma == 6 or config.charisma == 7:
        config.Deception += -2
        config.Intimidation += -2
        config.Performance += -2
        config.Persuasion += -2
        config.charismaMod = -2

    elif config.charisma == 8 or config.charisma == 9:
        config.Deception += -1
        config.Intimidation += -1
        config.Performance += -1
        config.Persuasion += -1
        config.charismaMod = -1

    elif config.charisma == 10 or config.charisma == 11:
        config.Deception += 0
        config.Intimidation += 0
        config.Performance += 0
        config.Persuasion += 0
        config.charismaMod = 0

    elif config.charisma == 12 or config.charisma == 13:
        config.Deception += 1
        config.Intimidation += 1
        config.Performance += 1
        config.Persuasion += 1
        config.charismaMod = 1

    elif config.charisma == 14 or config.charisma == 15:
        config.Deception += 2
        config.Intimidation += 2
        config.Performance += 2
        config.Persuasion += 2
        config.charismaMod = 2

    elif config.charisma == 16 or config.charisma == 17:
        config.Deception += 3
        config.Intimidation += 3
        config.Performance += 3
        config.Persuasion += 3
        config.charismaMod = 3

    elif config.charisma == 18 or config.charisma == 19:
        config.Deception += 4
        config.Intimidation += 4
        config.Performance += 4
        config.Persuasion += 4
        config.charismaMod = 4

    elif config.charisma >= 20:
        config.Deception += 5
        config.Intimidation += 5
        config.Performance += 5
        config.Persuasion += 5
        config.charismaMod = 5

    else:
        Error()


# This function converts the ability points into skill points for Wisdom
def WisdomConversion():
    if config.wisdom == 1:
        config.AnimalHandling = -5
        config.Insight = -5
        config.Medicine = -5
        config.Perception = -5
        config.Survival = -5
        config.wisdomMod = -5

    elif config.wisdom == 2 or config.wisdom == 3:
        config.AnimalHandling = -4
        config.Insight = -4
        config.Medicine = -4
        config.Perception = -4
        config.Survival = -4
        config.wisdomMod = -4

    elif config.wisdom == 4 or config.wisdom == 5:
        config.AnimalHandling = -3
        config.Insight = -3
        config.Medicine = -3
        config.Perception = -3
        config.Survival = -3
        config.wisdomMod = -3

    elif config.wisdom == 6 or config.wisdom == 7:
        config.AnimalHandling = -2
        config.Insight = -2
        config.Medicine = -2
        config.Perception = -2
        config.Survival = -2
        config.wisdomMod = -2

    elif config.wisdom == 8 or config.wisdom == 9:
        config.AnimalHandling = -1
        config.Insight = -1
        config.Medicine = -1
        config.Perception = -1
        config.Survival = -1
        config.wisdomMod = -1

    elif config.wisdom == 10 or config.wisdom == 11:
        config.AnimalHandling = 0
        config.Insight = 0
        config.Medicine = 0
        config.Perception = 0
        config.Survival = 0
        config.wisdomMod = 0

    elif config.wisdom == 12 or config.wisdom == 13:
        config.AnimalHandling = 1
        config.Insight = 1
        config.Medicine = 1
        config.Perception = 1
        config.Survival = 1
        config.wisdomMod = 1

    elif config.wisdom == 14 or config.wisdom == 15:
        config.AnimalHandling = 2
        config.Insight = 2
        config.Medicine = 2
        config.Perception = 2
        config.Survival = 2
        config.wisdomMod = 2

    elif config.wisdom == 16 or config.wisdom == 17:
        config.AnimalHandling = 3
        config.Insight = 3
        config.Medicine = 3
        config.Perception = 3
        config.Survival = 3
        config.wisdomMod = 3

    elif config.wisdom == 18 or config.wisdom == 19:
        config.AnimalHandling = 4
        config.Insight = 4
        config.Medicine = 4
        config.Perception = 4
        config.Survival = 4
        config.wisdomMod = 4

    elif config.wisdom >= 20:
        config.AnimalHandling = 5
        config.Insight = 5
        config.Medicine = 5
        config.Perception = 5
        config.Survival = 5
        config.wisdomMod = 5

    else:
        Error()


# This function converts the ability points into skill points for Dexterity
def DexterityConversion():
    global dexterity

    global Acrobatics
    global SleightOfHand
    global Stealth

    if config.dexterity == 1:
        config.Acrobatics = -5
        config.SleightOfHand = -5
        config.Stealth = -5
        config.dexterityMod = -5

    elif config.dexterity == 2 or config.dexterity == 3:
        config.Acrobatics = -4
        config.SleightOfHand = -4
        config.Stealth = -4
        config.dexterityMod = -4

    elif config.dexterity == 4 or config.dexterity == 5:
        config.Acrobatics = -3
        config.SleightOfHand = -3
        config.Stealth = -3
        config.dexterityMod = -3

    elif config.dexterity == 6 or config.dexterity == 7:
        config.Acrobatics = -2
        config.SleightOfHand = -2
        config.Stealth = -2
        config.dexterityMod = -2

    elif config.dexterity == 8 or config.dexterity == 9:
        config.Acrobatics = -1
        config.SleightOfHand = -1
        config.Stealth = -1
        config.dexterityMod = -1

    elif config.dexterity == 10 or config.dexterity == 11:
        config.Acrobatics = 0
        config.SleightOfHand = 0
        config.Stealth = 0
        config.dexterityMod = 0

    elif config.dexterity == 12 or config.dexterity == 13:
        config.Acrobatics = 1
        config.SleightOfHand = 1
        config.Stealth = 1
        config.dexterityMod = 1

    elif config.dexterity == 14 or config.dexterity == 15:
        config.Acrobatics = 2
        config.SleightOfHand = 2
        config.Stealth = 2
        config.dexterityMod = 2

    elif config.dexterity == 16 or config.dexterity == 17:
        config.Acrobatics = 3
        config.SleightOfHand = 3
        config.Stealth = 3
        config.dexterityMod = 3

    elif config.dexterity == 18 or config.dexterity == 19:
        config.Acrobatics = 4
        config.SleightOfHand = 4
        config.Stealth = 4
        config.dexterityMod = 4

    elif config.dexterity >= 20:
        config.Acrobatics = 5
        config.SleightOfHand = 5
        config.Stealth = 5
        config.dexterityMod = 5

    else:
        Error()


# This function converts the ability points into skill points for Intelligence
def IntelligenceConversion():

    if config.intelligence == 1:
        config.Arcana = -5
        config.History = -5
        config.Investigation = -5
        config.Nature = -5
        config.Religion = -5
        config.IntelliMod = -5

    elif config.intelligence == 2 or config.intelligence == 3:
        config.Arcana = -4
        config.History = -4
        config.Investigation = -4
        config.Nature = -4
        config.Religion = -4
        config.IntelliMod = -4

    elif config.intelligence == 4 or config.intelligence == 5:
        config.Arcana = -3
        config.History = -3
        config.Investigation = -3
        config.Nature = -3
        config.Religion = -3
        config.IntelliMod = -3

    elif config.intelligence == 6 or config.intelligence == 7:
        config.Arcana = -2
        config.History = -2
        config.Investigation = -2
        config.Nature = -2
        config.Religion = -2
        config.IntelliMod = -2

    elif config.intelligence == 8 or config.intelligence == 9:
        config.Arcana = -1
        config.History = -1
        config.Investigation = -1
        config.Nature = -1
        config.Religion = -1
        config.IntelliMod = -1

    elif config.intelligence == 10 or config.intelligence == 11:
        config.Arcana = 0
        config.History = 0
        config.Investigation = 0
        config.Nature = 0
        config.Religion = 0
        config.IntelliMod = 0

    elif config.intelligence == 12 or config.intelligence == 13:
        config.Arcana = 1
        config.History = 1
        config.Investigation = 1
        config.Nature = 1
        config.Religion = 1
        config.IntelliMod = 1

    elif config.intelligence == 14 or config.intelligence == 15:
        config.Arcana = 2
        config.History = 2
        config.Investigation = 2
        config.Nature = 2
        config.Religion = 2
        config.IntelliMod = 2

    elif config.intelligence == 16 or config.intelligence == 17:
        config.Arcana = 3
        config.History = 3
        config.Investigation = 3
        config.Nature = 3
        config.Religion = 3
        config.IntelliMod = 3

    elif config.intelligence == 18 or config.intelligence == 19:
        config.Arcana = 4
        config.History = 4
        config.Investigation = 4
        config.Nature = 4
        config.Religion = 4
        config.IntelliMod = 4

    elif config.intelligence >= 20:
        config.Arcana = 5
        config.History = 5
        config.Investigation = 5
        config.Nature = 5
        config.Religion = 5
        config.IntelliMod = 5

    else:
        Error()


# This function converts the ability points into a modifier
def ConstitutionConversion():

    if config.constitution == 1:
        config.constitutionMod += -5

    elif config.constitution == 2 or config.constitution == 3:
        config.constitutionMod += -4

    elif config.constitution == 4 or config.constitution == 5:
        config.constitutionMod += -3

    elif config.constitution == 6 or config.constitution == 7:
        config.constitutionMod += -2

    elif config.constitution == 8 or config.constitution == 9:
        config.constitutionMod += -1

    elif config.constitution == 10 or config.constitution == 11:
        config.constitutionMod += 0

    elif config.constitution == 12 or config.constitution == 13:
        config.constitutionMod += 1

    elif config.constitution == 14 or config.constitution == 15:
        config.constitutionMod += 2

    elif config.constitution == 16 or config.constitution == 17:
        config.constitutionMod += 3

    elif config.constitution == 18 or config.constitution == 19:
        config.constitutionMod += 4

    elif config.constitution >= 20:
        config.constitutionMod += 5

    else:
        Error()


# This function calculates the HP
def HPconversion():

    ConstitutionConversion()

    if config.temp_r == 1:
        # Barbarian
        dice = random.randint(1, 12)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 2:
        # Bard
        dice = random.randint(1, 8)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 3:
        # Cleric
        dice = random.randint(1, 8)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 4:
        # Druid
        dice = random.randint(1, 8)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 5:
        # Fighter
        dice = random.randint(1, 10)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 6:
        # Monk
        dice = random.randint(1, 8)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 7:
        # Paladin
        dice = random.randint(1, 10)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 8:
        # Ranger
        dice = random.randint(1, 10)
        config.hp = (dice * config.lvl) + (config.constitutionMod * config.lvl)

    elif config.temp_r == 9:
        # Rogue
        dice = random.randint(1, 8)
        config.hp = (dice * config.lvl) + (config.constitution * config.lvl)

    elif config.temp_r == 10:
        # Sorcerer
        dice = random.randint(1, 6)
        config.hp = (dice * config.lvl) + (config.constitution * config.lvl)

    elif config.temp_r == 11:
        # Warlock
        dice = random.randint(1, 8)
        config.hp = (dice * config.lvl) + (config.constitution * config.lvl)

    elif config.temp_r == 12:
        # Wizard
        dice = random.randint(1, 6)
        config.hp = (dice * config.lvl) + (config.constitution * config.lvl)

    else:
        Error()


#This function calculates the saving throws
def SavingThrows():
    if config.temp_r == 1:
        # Barbarian
        config.ST_strength = config.strengthMod + config.cache
        config.ST_constitution = config.constitutionMod + config.cache
        config.ST_charisma = config.charismaMod
        config.ST_wisdom = config.wisdomMod
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod


    elif config.temp_r == 2:
        # Bard
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod + config.cache
        config.ST_wisdom = config.wisdomMod
        config.ST_dexterity = config.dexterityMod + config.cache
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 3:
        # Cleric
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod + config.cache
        config.ST_wisdom = config.wisdomMod + config.cache
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 4:
        # Druid
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod
        config.ST_wisdom = config.wisdomMod + config.cache
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod + config.cache

    elif config.temp_r == 5:
        # Fighter
        config.ST_strength = config.strengthMod + config.cache
        config.ST_constitution = config.constitutionMod + config.cache
        config.ST_charisma = config.charismaMod
        config.ST_wisdom = config.wisdomMod
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 6:
        # Monk
        config.ST_strength = config.strengthMod + config.cache
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod
        config.ST_wisdom = config.wisdomMod
        config.ST_dexterity = config.dexterityMod + config.cache
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 7:
        # Paladin
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod + config.cache
        config.ST_wisdom = config.wisdomMod + config.cache
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 8:
        # Ranger
        config.ST_strength = config.strengthMod + config.cache
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod
        config.ST_wisdom = config.wisdomMod
        config.ST_dexterity = config.dexterityMod + config.cache
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 9:
        # Rogue
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod
        config.ST_wisdom = config.wisdomMod
        config.ST_dexterity = config.dexterityMod + config.cache
        config.ST_intelligence = config.IntelliMod + config.cache

    elif config.temp_r == 10:
        # Sorcerer
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod + config.cache
        config.ST_charisma = config.charismaMod + config.cache
        config.ST_wisdom = config.wisdomMod
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 11:
        # Warlock
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod + config.cache
        config.ST_wisdom = config.wisdomMod + config.cache
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod

    elif config.temp_r == 12:
        # Wizard
        config.ST_strength = config.strengthMod
        config.ST_constitution = config.constitutionMod
        config.ST_charisma = config.charismaMod
        config.ST_wisdom = config.wisdomMod + config.cache
        config.ST_dexterity = config.dexterityMod
        config.ST_intelligence = config.IntelliMod + config.cache

    else:
        Error()

# This function defines what the program will do in case of an error or unexpected case
def Error():
    print("There was an unknown error. Please try again")
    quit()