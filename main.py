import csv
import random
from array import *

def Menu():
    print("D&D Sheet Builder\n 1 - Character creation\n 2 - Party Creation\n 3 - GM Viewer\n")
    index = int(input("Enter the value: "))
    if index == 1:
        CharacterCreation()
    else:
        print("Incorrect answer. Try again")
        Menu()

class Character:
  def __init__(self, name, race,Class, level, strength, dexterity, constitution, wisdom, intelligence, charisma):
    self.name = name
    self.race = race
    self.Class = Class
    self.level = level
    self.Strength = strength
    self.Dexterity = dexterity
    self.Constitution = constitution
    self.Wisdom = wisdom
    self.Intelligence = intelligence
    self.Charisma = charisma


def raceTranslation():
    global race
    global temp_r

    global temp_str2
    global temp_dex2
    global temp_const2
    global temp_wis2
    global temp_intelli2
    global temp_charisma2

    if temp_r == 1:
        race = "Dragonborn"
        temp_str2 = 2
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0 
        temp_intelli2 = 0
        temp_charisma2 = 1

    elif temp_r == 2:
        race = "Dwarf"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 2
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 3:
        race = "Elf"
        temp_str2 = 0
        temp_dex2 = 2
        temp_const2 = 0 
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 4:
        race = "Gnome"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 2
        temp_charisma2 = 0

    elif temp_r == 5:
        race = "Half-Elf"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 2

        for i in range(2):
            print("Because you've chosen Half-Elf, you can increase 2 ability scores by 1.\n 1 for Strength\n 2 for Dexterity\n 3 for Constitution\n 4 for Wisdom\n 5 for Intelligence\n")
            option = int(input("Type your answer: "))
            if option == 1:
                temp_str2 += 1
            if option == 2:
                temp_dex2 += 1
            if option == 3:
                temp_const2 += 1
            if option == 4:
                temp_wis2 += 1
            if option == 5:
                temp_intelli2 += 1
            else:
                print("Error: Something went wrong")

    elif temp_r == 6:
        race = "Halfling"
        temp_str2 = 0
        temp_dex2 = 2
        temp_const2 = 0
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 7:
        race = "Half-Orc"
        temp_str2 = 2
        temp_dex2 = 0
        temp_const2 = 1
        temp_wis2 = 0
        temp_intelli2 = 0
        temp_charisma2 = 0

    elif temp_r == 8:
        race = "Human"
        temp_str2 = 1
        temp_dex2 = 1
        temp_const2 = 1
        temp_wis2 = 1
        temp_intelli2 = 1
        temp_charisma2 = 1

    elif temp_r == 9:
        race = "Tiefling"
        temp_str2 = 0
        temp_dex2 = 0
        temp_const2 = 0
        temp_wis2 = 0 
        temp_intelli2 = 1
        temp_charisma2 = 2

    else:
        print("Something went wrong.")

def classTranslation():
    global Class
    global temp_c
    if temp_c == 1:
        Class = "Barbarian"
    elif temp_c == 2:
        Class = "Bard"
    elif temp_c == 3:
        Class = "Cleric"
    elif temp_c == 4:
        Class = "Druid"
    elif temp_c == 5:
        Class = "Fighter"
    elif temp_c == 6:
        Class = "Monk"
    elif temp_c == 7:
        Class = "Paladin"
    elif temp_c == 8:
        Class = "Ranger"
    elif temp_c == 9:
        Class = "Rogue"
    elif temp_c == 10:
        Class = "Sorcerer"
    elif temp_c == 11:
        Class = "Warlock"
    elif temp_c == 12:
        Class = "Wizard"
    else:
        print("Something went wrong.")

def rollDice():
    
    numArray = array ('i',[])

    for i in range(4): 
        num = random.randint(1,6)
        numArray.append(num)

    numArray = sorted(numArray)
    highest_sum = numArray[1] + numArray[2] + numArray[3] 
    return highest_sum


def CharacterCreation():
    global temp_r
    global temp_c

    global temp_str2
    global temp_dex2
    global temp_const2
    global temp_wis2
    global temp_intelli2
    global temp_charisma2

    name = str(input("Character name: "))
    temp_r = int(input("\nChoose a race\n 1 - Dragonborn\n 2 - Dwarf\n 3 - Elf\n 4 - Gnome\n 5 - Half-Elf\n 6 - Halfling\n 7 - Half-Orc\n 8 - Human\n 9 - Tiefling\n Type your answer: "))
    temp_c = int(input("\nChoose a class\n 1 - Barbarian\n 2 - Bard\n 3 - Cleric\n 4 - Druid\n 5 - Fighter\n 6 - Monk\n 7 - Paladin\n 8 - Ranger\n 9 - Rogue\n 10 - Sorcerer\n 11 - Warlock\n 12 - Wizard\n Type your answer: "))
    lvl = int(input("Set the level: "))
    
    raceTranslation()

    temp_strength = rollDice()
    strength = temp_strength + temp_str2

    temp_dexterity = rollDice()
    dexterity = temp_dexterity + temp_dex2

    temp_constitution = rollDice()
    constitution = temp_constitution + temp_const2

    temp_wisdom = rollDice()
    wisdom = temp_wisdom + temp_wis2

    temp_intelligence = rollDice()
    intelligence = temp_intelligence + temp_intelli2

    temp_charisma = rollDice()
    charisma = temp_charisma + temp_charisma2

    print("temp_1 ", temp_strength, temp_str2)
    print("temp_2 ", temp_intelligence, temp_intelli2)
    classTranslation()

    char = Character(name,race,Class,lvl,strength,dexterity,constitution,wisdom,intelligence,charisma)
    print(char.name)
    print(char.race)
    print(char.Class)
    print(char.level)
    print(char.Strength)
    print(char.Dexterity)
    print(char.Constitution)
    print(char.Wisdom)
    print(char.Intelligence)
    print(char.Charisma)

Menu()

