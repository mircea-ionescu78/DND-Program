import random
from array import *
import os
import csv

from bin.functions import *
import config




# This is the function defining the main menu
def Menu():
    print(
"\n\n██████████   ██████   █████ ██████████      ███████████\n"                                                               
"░░███░░░░███ ░░██████ ░░███ ░░███░░░░███    ░░███░░░░░███\n"                                                               
"░███   ░░███ ░███░███ ░███  ░███   ░░███    ░███    ░███ ████████   ██████   ███████ ████████   ██████   █████████████\n"  
"░███    ░███ ░███░░███░███  ░███    ░███    ░██████████ ░░███░░███ ███░░███ ███░░███░░███░░███ ░░░░░███ ░░███░░███░░███\n" 
"░███    ░███ ░███ ░░██████  ░███    ░███    ░███░░░░░░   ░███ ░░░ ░███ ░███░███ ░███ ░███ ░░░   ███████  ░███ ░███ ░███\n"
"░███    ███  ░███  ░░█████  ░███    ███     ░███         ░███     ░███ ░███░███ ░███ ░███      ███░░███  ░███ ░███ ░███\n"
"██████████   █████  ░░█████ ██████████      █████        █████    ░░██████ ░░███████ █████    ░░████████ █████░███ █████\n"
"░░░░░░░░░░   ░░░░░    ░░░░░ ░░░░░░░░░░      ░░░░░        ░░░░░      ░░░░░░   ░░░░░███░░░░░      ░░░░░░░░ ░░░░░ ░░░ ░░░░░\n" 
"                                                                             ███ ░███                                   \n"
"                                                                            ░░██████                                    \n"
"                                                                             ░░░░░░                                      \n")
    print("\n 1 - Character creation\n 2 - Party Creation\n 3 - Game Master Viewer\n 4 - Quit\n")
    index = int(input("Enter the value: "))
    if index == 0:
        print("\n")
    elif index == 1:
        CharacterCreation()
    elif index == 2:
        party_creation()
    elif index == 3:
        load_char()
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
    # Old system
    file = open("characters.txt", "a")
    save = str(char.name) + " , " + str(char.race) + " , " + str(char.Class) + " , " + str(char.level) + " , " + str(char.Strength) + " , " + str(char.Dexterity) + " , " + str(char.Constitution) + " , " + str(char.Wisdom) + " , " + str(char.Intelligence) + " , " + str(char.Charisma) + "\n"
    file.write(save)
    # New system
    file_name = os.path.join("characters/", f"{char.name}.csv")
    file2 = open(file_name, 'a', newline='')
    writer = csv.writer(file2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([char.name])
    writer.writerow([char.race])
    writer.writerow([char.Class])
    writer.writerow([char.level])
    writer.writerow([char.Strength])
    writer.writerow([char.Dexterity])
    writer.writerow([char.Constitution])
    writer.writerow([char.Wisdom])
    writer.writerow([char.Intelligence])
    writer.writerow([char.Charisma])
    writer.writerow([char.Athletics])
    writer.writerow([char.Acrobatics])
    writer.writerow([char.SleightOfHand])
    writer.writerow([char.Stealth])
    writer.writerow([char.Arcana])
    writer.writerow([char.History])
    writer.writerow([char.Investigation])
    writer.writerow([char.AnimalHandling])
    writer.writerow([char.Intimidation])
    writer.writerow([char.Nature])
    writer.writerow([char.Religion])
    writer.writerow([char.Perception])
    writer.writerow([char.Survival])
    writer.writerow([char.Insight])
    writer.writerow([char.Medicine])
    writer.writerow([char.Deception])
    writer.writerow([char.Persuasion])
    writer.writerow([char.Performance])


def party_creation():
    characters = len(os.listdir('characters'))
    if characters == 0:
        print("There needs to be a minimum of 1 character created to access this menu")
        Menu()
    else:
        party_name = str(input("Name the party: "))
        print(f"{characters} available characters in the folder")
        party_size = int(input("How many members are in the party? - "))

        if party_size > 6:
            Error()
        else:
            party_char1 = str(input("Enter the character name: "))
            party_char2 = str(input("Enter the character name: "))
            party_char3 = str(input("Enter the character name: "))
            party_char4 = str(input("Enter the character name: "))
            party_char5 = str(input("Enter the character name: "))
            if party_char1 == "":
                Error()
            elif party_char2 == "":
                print("Cannot make a party of only one member")
                Error()
            elif party_char3 == '' and party_char4 == '' and party_char5 == '':
                print("Party made only with 2 characters")
            elif party_char4 == '' and party_char5 == '':
                print("Party made only with 3 characters")
            elif party_char4 != "" and party_char5 == '':
                print("Party made only with 4 characters")
            else:
                print("Party made with 5 characters")


def load_char():
    char1 = []
    print("\nIn order to load a character, you need to choose what character to import.")
    option = str(input("Input the character name: "))
    file_name = os.path.join("characters/", f"{option}.csv")
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            row = str(row)
            char1.append(row)

    print("Name: ", char1[0])
    print("Race: ", char1[1])
    print("Class: ", char1[2])
    print("Level: ", char1[3])
    print("========================")
    print("Strength: ", char1[4])
    print("Dexterity: ", char1[5])
    print("Constitution: ", char1[6])
    print("Wisdom: ", char1[7])
    print("Intelligence: ", char1[8])
    print("Charisma: ", char1[9])
    print("========================")
    see_more = str(input("Do you want to see more? y/n"))
    if see_more == "y":
        print("**Strength**")
        print("Athletics: ", char1[10])
        print("**Dexterity**")
        print("Acrobatics: ", char1[11])
        print("Sleight of Hand: ", char1[12])
        print("Stealth: ", char1[13])
        print("**Intelligence**")
        print("Arcana: ", char1[8])
        print("Charisma: ", char1[9])
        print("========================")


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
