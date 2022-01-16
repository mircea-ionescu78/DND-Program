import random
from array import *

from bin.functions import *
import config


# This is the function defining the main menu
def Menu():
    print("\n ========================\nD&D Sheet Builder\n ========================\n 1 - Character creation\n 2 - Party Creation\n 3 - Game Master Viewer\n 4 - Quit\n")
    index = int(input("Enter the value: "))
    if index == 0:
        print("\n")
    elif index == 1:
        CharacterCreation()
    elif index == 3:
        CharacterCreation()
    elif index == 4:
        quit()
    else:
        print("Incorrect answer. Try again")
        Menu()


# This is the class defining the character template
class Character:

    def __init__(self, name, race, Class, level, strength, dexterity, constitution, wisdom,
                 intelligence, charisma, Athletics, Acrobatics, SleightOfHand, Stealth, Arcana, History,
                 Investigation, AnimalHandling, Intimidation, Nature, Religion, Perception, Survival,
                 Insight, Medicine, Deception, Persuasion, Performance):
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
        self.AnimalHandling = AnimalHandling
        self.Intimidation = Intimidation
        self.Nature = Nature
        self.Religion = Religion
        self.Perception = Perception
        self.Survival = Survival
        self.Insight = Insight
        self.Medicine = Medicine
        self.Deception = Deception
        self.Persuasion = Persuasion
        self.Performance = Performance


# This function saves the character in the characters.txt
def saveChar():
    file = open("characters.txt", "a")
    save = str(char.name) + " , " + str(char.race) + " , " + str(char.Class) + " , " + str(char.level) + " , " + str(char.Strength) + " , " + str(char.Dexterity) + " , " + str(char.Constitution) + " , " + str(char.Wisdom) + " , " + str(char.Intelligence) + " , " + str(char.Charisma) + "\n"
    file.write(save)


# This function defines the character creation process
def CharacterCreation():
    global char

    config.name = str(input("Character name: "))
    config.temp_r = int(input("\nChoose a race\n "
                              "1 - Dragonborn\n "
                              "2 - Dwarf\n "
                              "3 - Elf\n "
                              "4 - Gnome\n "
                              "5 - Half-Elf\n "
                              "6 - Halfling\n "
                              "7 - Half-Orc\n "
                              "8 - Human\n "
                              "9 - Tiefling\n "
                              "Type your answer: "))

    config.temp_c = int(input("\nChoose a class\n "
                              "1 - Barbarian\n "
                              "2 - Bard\n "
                              "3 - Cleric\n "
                              "4 - Druid\n "
                              "5 - Fighter\n "
                              "6 - Monk\n "
                              "7 - Paladin\n "
                              "8 - Ranger\n "
                              "9 - Rogue\n "
                              "10 - Sorcerer\n "
                              "11 - Warlock\n "
                              "12 - Wizard\n"
                              " Type your answer: "))

    config.lvl = int(input("Set the level: "))

    raceTranslation()

    temp_strength = rollDice()
    config.strength = temp_strength + config.temp_str2

    temp_dexterity = rollDice()
    config.dexterity = temp_dexterity + config.temp_dex2

    temp_constitution = rollDice()
    config.constitution = temp_constitution + config.temp_const2

    temp_wisdom = rollDice()
    config.wisdom = temp_wisdom + config.temp_wis2

    temp_intelligence = rollDice()
    config.intelligence = temp_intelligence + config.temp_intelli2

    temp_charisma = rollDice()
    config.charisma = temp_charisma + config.temp_charisma2

    LevelConversion()

    StrengthConversion()
    CharismaConversion()
    WisdomConversion()
    IntelligenceConversion()
    DexterityConversion()

    classTranslation()

    char = Character(config.name, config.race, config.Class, config.lvl, config.strength, config.dexterity, config.constitution, config.wisdom, config.intelligence,
                     config.charisma, config.Athletics, config.Acrobatics, config.SleightOfHand, config.Stealth, config.Arcana, config.History, config.Investigation,
                     config.AnimalHandling, config.Intimidation, config.Nature, config.Religion, config.Perception, config.Survival, config.Insight, config.Medicine,
                     config.Deception, config.Persuasion, config.Performance)

    saveChar()

    Menu()


Menu()
