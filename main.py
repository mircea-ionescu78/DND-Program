import random
from array import *
import os
import functions
import config

cache = 0
AnimalHandling = 0
Athletics = 0
Acrobatics = 0
SleightOfHand = 0
Stealth = 0
Arcana = 0
History = 0
Investigation = 0

#This is the function defining the main menu
def Menu():
    print("D&D Sheet Builder\n 1 - Character creation\n 2 - Party Creation\n 3 - GM Viewer\n 4 - Quit\n")
    index = int(input("Enter the value: "))

    if index == 1:
        CharacterCreation()
    elif index == 4:
        quit()
    else:
        print("Incorrect answer. Try again")
        Menu()

#This is the class defining the character template
class Character:

    def __init__(self, name, race, Class, level, strength, dexterity, constitution, wisdom, intelligence, charisma, Athletics, Acrobatics, SleightOfHand, Stealth, Arcana, History, Investigation):
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
        self.Athletics = Athletics
        self.Acrobatics = Acrobatics
        self.SleightOfHand = SleightOfHand
        self.Stealth = Stealth
        self.Arcana = Arcana
        self.History = History
        self.Investigation = Investigation


# This function would save the character in the characters.txt
def saveChar():
    file = open("characters.txt", "a")
    save = str(char.name) + " , " + str(char.race) + " , " + str(char.Class) + " , " + str(char.level) + " , " + str(char.Strength) + " , " + str(char.Dexterity) + " , " + str(char.Constitution) + " , " + str(char.Wisdom) + " , " + str(char.Intelligence) + " , " + str(char.Charisma) + "\n"
    file.write(save)


def StrengthConversion():
    global strength
    global Athletics

    if strength == 1:
        Athletics = -5

    elif strength == 2 or strength == 3:
        Athletics = -4

    elif strength == 4 or strength == 5:
        Athletics = -3

    elif strength == 6 or strength == 7:
        Athletics = -2

    elif strength == 8 or strength == 9:
        Athletics = -1

    elif strength == 10 or strength == 11:
        Athletics = 0

    elif strength == 12 or strength == 13:
        Athletics = 1

    elif strength == 14 or strength == 15:
        Athletics = 2

    elif strength == 16 or strength == 17:
        Athletics = 3

    elif strength == 18 or strength == 19:
        Athletics = 4

    elif strength >= 20:
         Athletics = 5


def DexterityConversion():
    global dexterity

    global Acrobatics
    global SleightOfHand
    global Stealth

    if dexterity == 1:
        Acrobatics  = -5
        SleightOfHand = -5
        Stealth = -5

    elif dexterity == 2 or dexterity == 3:
        Acrobatics = -4
        SleightOfHand = -4
        Stealth = -4

    elif dexterity == 4 or dexterity == 5:
        Acrobatics = -3
        SleightOfHand = -3
        Stealth = -3

    elif dexterity == 6 or dexterity == 7:
        Acrobatics = -2
        SleightOfHand = -2
        Stealth = -2

    elif dexterity == 8 or dexterity == 9:
        Acrobatics = -1
        SleightOfHand = -1
        Stealth = -1

    elif dexterity == 10 or dexterity == 11:
        Acrobatics = 0
        SleightOfHand = 0
        Stealth = 0

    elif dexterity == 12 or dexterity == 13:
        Acrobatics = 1
        SleightOfHand = 1
        Stealth = 1

    elif dexterity == 14 or dexterity == 15:
        Acrobatics = 2
        SleightOfHand = 2
        Stealth = 2

    elif dexterity == 16 or dexterity == 17:
        Acrobatics = 3
        SleightOfHand = 3
        Stealth = 3

    elif dexterity == 18 or dexterity == 19:
        Acrobatics = 4
        SleightOfHand = 4
        Stealth = 4

    elif dexterity >= 20:
        Acrobatics = 5
        SleightOfHand = 5
        Stealth = 5


def IntelligenceConversion():

    global intelligence

    global Arcana
    global History
    global Investigation
    global Nature
    global Religion

    if intelligence == 1:
        Arcana = -5
        History = -5
        Investigation = -5
        Nature = -5
        Religion = -5

    elif intelligence == 2 or intelligence == 3:
        Arcana = -4
        History = -4
        Investigation = -4
        Nature = -4
        Religion = -4

    elif intelligence == 4 or intelligence == 5:
        Arcana = -3
        History = -3
        Investigation = -3
        Nature = -3
        Religion = -3

    elif intelligence == 6 or intelligence == 7:
        Arcana = -2
        History = -2
        Investigation = -2
        Nature = -2
        Religion = -2

    elif intelligence == 8 or intelligence == 9:
        Arcana = -1
        History = -1
        Investigation = -1
        Nature = -1
        Religion = -1

    elif intelligence == 10 or intelligence == 11:
        Arcana = 0
        History = 0
        Investigation = 0
        Nature = 0
        Religion = 0

    elif intelligence == 12 or intelligence == 13:
        Arcana = 1
        History = 1
        Investigation = 1
        Nature = 1
        Religion = 1

    elif intelligence == 14 or intelligence == 15:
        Arcana = 2
        History = 2
        Investigation = 2
        Nature = 2
        Religion = 2

    elif intelligence == 16 or intelligence == 17:
        Arcana = 3
        History = 3
        Investigation = 3
        Nature = 3
        Religion = 3

    elif intelligence == 18 or intelligence == 19:
        Arcana = 4
        History = 4
        Investigation = 4
        Nature = 4
        Religion = 4

    elif intelligence >= 20:
        Arcana = 5
        History = 5
        Investigation = 5
        Nature = 5
        Religion = 5


def WisdomConversion():
    global wisdom

    global AnimalHandling
    global Insight
    global Medicine
    global Perception
    global Survival

    if wisdom == 1:
        AnimalHandling = -5
        Insight = -5
        Medicine = -5
        Perception = -5
        Survival = -5

    elif wisdom == 2 or wisdom == 3:
        AnimalHandling = -4
        Insight = -4
        Medicine = -4
        Perception = -4
        Survival = -4

    elif wisdom == 4 or wisdom == 5:
        AnimalHandling = -3
        Insight = -3
        Medicine = -3
        Perception = -3
        Survival = -3

    elif wisdom == 6 or wisdom == 7:
        AnimalHandling = -2
        Insight = -2
        Medicine = -2
        Perception = -2
        Survival = -2

    elif wisdom == 8 or wisdom == 9:
        AnimalHandling = -1
        Insight = -1
        Medicine = -1
        Perception = -1
        Survival = -1

    elif wisdom == 10 or wisdom == 11:
        AnimalHandling = 0
        Insight = 0
        Medicine = 0
        Perception = 0
        Survival = 0

    elif wisdom == 12 or wisdom == 13:
        AnimalHandling = 1
        Insight = 1
        Medicine = 1
        Perception = 1
        Survival = 1

    elif wisdom == 14 or wisdom == 15:
        AnimalHandling = 2
        Insight = 2
        Medicine = 2
        Perception = 2
        Survival = 2

    elif wisdom == 16 or wisdom == 17:
        AnimalHandling = 3
        Insight = 3
        Medicine = 3
        Perception = 3
        Survival = 3

    elif wisdom == 18 or wisdom == 19:
        AnimalHandling = 4
        Insight = 4
        Medicine = 4
        Perception = 4
        Survival = 4

    elif wisdom >= 20:
        AnimalHandling = 5
        Insight = 5
        Medicine = 5
        Perception = 5
        Survival = 5


def CharismaConversion():

    global charisma

    global Deception
    global Intimidation
    global Performance
    global Persuasion

    if charisma == 1:
        Deception = -5
        Intimidation = -5
        Performance = -5
        Persuasion = -5


    elif charisma == 2 or charisma == 3:
        Deception = -4
        Intimidation = -4
        Performance = -4
        Persuasion = -4


    elif charisma == 4 or charisma == 5:
        Deception = -3
        Intimidation = -3
        Performance = -3
        Persuasion = -3


    elif charisma == 6 or charisma == 7:
        Deception = -2
        Intimidation = -2
        Performance = -2
        Persuasion = -2


    elif charisma == 8 or charisma == 9:
        Deception = -1
        Intimidation = -1
        Performance = -1
        Persuasion = -1


    elif charisma == 10 or charisma == 11:
        Deception = 0
        Intimidation = 0
        Performance = 0
        Persuasion = 0


    elif charisma == 12 or charisma == 13:
        Deception = 1
        Intimidation = 1
        Performance = 1
        Persuasion = 1


    elif charisma == 14 or charisma == 15:
        Deception = 2
        Intimidation = 2
        Performance = 2
        Persuasion = 2


    elif charisma == 16 or charisma == 17:
        Deception = 3
        Intimidation = 3
        Performance = 3
        Persuasion = 3


    elif charisma == 18 or charisma == 19:
        Deception = 4
        Intimidation = 4
        Performance = 4
        Persuasion = 4

    elif charisma >= 20:
        Deception = 5
        Intimidation = 5
        Performance = 5
        Persuasion = 5


def CharacterCreation():
    global temp_r
    global temp_c
    global char
    global temp_str2
    global temp_dex2
    global temp_const2
    global temp_wis2
    global temp_intelli2
    global temp_charisma2
    global lvl

    global strength
    global dexterity
    global constitution
    global wisdom
    global intelligence
    global charisma
    global race

    global Athletics
    global Acrobatics
    global SleightOfHand
    global Stealth
    global Arcana
    global History
    global Investigation

    config.name = str(input("Character name: "))
    config.temp_r = int(input("\nChoose a race\n 1 - Dragonborn\n 2 - Dwarf\n 3 - Elf\n 4 - Gnome\n 5 - Half-Elf\n 6 - Halfling\n 7 - Half-Orc\n 8 - Human\n 9 - Tiefling\n Type your answer: "))
    config.temp_c = int(input("\nChoose a class\n 1 - Barbarian\n 2 - Bard\n 3 - Cleric\n 4 - Druid\n 5 - Fighter\n 6 - Monk\n 7 - Paladin\n 8 - Ranger\n 9 - Rogue\n 10 - Sorcerer\n 11 - Warlock\n 12 - Wizard\n Type your answer: "))
    config.lvl = int(input("Set the level: "))

    functions.raceTranslation()

    temp_strength = functions.rollDice()
    config.strength = temp_strength + config.temp_str2

    temp_dexterity = functions.rollDice()
    config.dexterity = temp_dexterity + config.temp_dex2

    temp_constitution = functions.rollDice()
    config.constitution = temp_constitution + config.temp_const2

    temp_wisdom = functions.rollDice()
    config.wisdom = temp_wisdom + config.temp_wis2

    temp_intelligence = functions.rollDice()
    config.intelligence = temp_intelligence + config.temp_intelli2

    temp_charisma = functions.rollDice()
    config.charisma = temp_charisma + config.temp_charisma2

    functions.LevelConversion()

    functions.classTranslation()

    char = Character(config.name, config.race, config.Class, config.lvl, config.strength, config.dexterity, config.constitution, config.wisdom, config.intelligence, config.charisma, config.Athletics, config.Acrobatics, config.SleightOfHand, config.Stealth, config.Arcana, config.History, config.Investigation)

    saveChar()


Menu()

