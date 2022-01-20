#Program: DnD character creation
#Programer: Jahson Gonzalez-Allie
#Description: This program will create a class that collects information to create a class. then it will tell 
#                   the inforamtion about the character and depending on its level it current skills. 

from os import readlink
from Character import menuClass
from Character import printCharacter
from Character import RaceClass
from Character import slowprint
from Character import slowerprint
from Character import diceroller
from Races.Dragonborn import DargonbornMain
import random

#needed for every class
import _json
#_json.dump()     empties data into .json file
#_json.load()     load data from .json file with all the varible 
#data file, only str
'''
import sys
import time
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
        '''
#file = open("data.txt",'a+')    #open file .txt "data" and "r+" allows to read
                                #"a+" allow to open/create and append file if file doesn't throws error
                                #file.trucate(0) delete character after number of character
                                #variable = file.readline() to get all info in the file as a list
                                    #for lines in 
'''
file = open("Artificer.txt",'r+')

for line in file:
    print(line)

file.close
'''

name = input("What is your characters name: ") #setname
clas = 0 #setClass
race = 0 #setRace
lv = (int(input("What is the characters level: "))) #setLevel #levelUp
levelup = 'yes' #query controll statement
display = 'yes' #query controll statement
more = 'Y'    #query controll statement
classHolder = 'Space' #Holds the classes name as a string in the Character class
raceHolder = 'Space'  #Holds the Races name as a string in the Character class
stat = []   #holds stats
sub = 0 #sets sub race
ele ='Blank'    #sets element of dragonborn
statImpro =[]
darkvison = 'Blank'
presence = 'Blank'
assult = 'Blank'
count = 0


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#level error trap
while (lv<=0 or lv>=21):
    print("Invaild option:")
    lv = (int(input("What is the characters level: ")))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#dice roller
more = 'Y'
MINSTAT = 70    
print("Rolling stats")
while(more[0].upper() == "Y"):
    stat=diceroller.stats()

    if (sum(stat)<MINSTAT):
        stat=diceroller.stats()
    
    print("What do you think about these stats\n",stat)
    more=input("Roll again?: ")

assign = diceroller.asssign(stat)

stat = [stat[i] for i in assign ]   #sets values from the stats rolled
Str = stat[0]
Dex = stat[1]
Con = stat[2]
Int = stat[3]
Wis = stat[4]
Cha = stat[5]


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#Race

RaceClass.menuRace()          #print table of races
race = int(input("Enter the numeber for your Race: "))
print("\n\n")

#Error trap for menu race
while (race<=0 or race>=9):
    print("Invaild option:")
    race = (int(input("Enter the number for your Race: \n\n")))

raceNum = race - 1 #puts the input in a way that the program can find the race string

if(race==1):
    sub = DargonbornMain.dragonBorn(sub)
    #menuRace.DragonbonDragonborn(race)      needs to be made
    race = RaceClass.setrace(raceHolder,raceNum)
    if(sub==1):
        upgrade = DargonbornMain.DragonbornStandard(Str,Cha)
        Str = upgrade[0]
        Cha = upgrade[1]
        sub = 'Standard'
        ele = upgrade[2]
    elif(sub==2):
        upgrade = DargonbornMain.DragonbornBlood(Int,Cha)
        Int = upgrade[0]
        Cha = upgrade[1]
        sub = 'Draconblood'
        ele = upgrade[2]
        
    elif(sub==3):
        upgrade = DargonbornMain.DragonbornRavenite(Str,Con)
        Str = upgrade[0]
        Con = upgrade[1]
        sub = 'Ravenite'
        ele = upgrade[2]

    elif(sub==4):
        upgrade = DargonbornMain.DragonChromatic(Str,Dex,Con,Int,Wis,Cha)
        Str = upgrade[0]
        Dex = upgrade[1]
        Con = upgrade[2]
        Int = upgrade[3]
        Wis = upgrade[4]
        Cha = upgrade[5]
        sub = 'Chromatic' 
        ele = upgrade[6]


    elif(sub==5):
        upgrade = DargonbornMain.DragonGem(Str,Dex,Con,Int,Wis,Cha)
        Str = upgrade[0]
        Dex = upgrade[1]
        Con = upgrade[2]
        Int = upgrade[3]
        Wis = upgrade[4]
        Cha = upgrade[5]
        sub = 'Gem'
        ele = upgrade[6]


    elif(sub==6):
        upgrade = DargonbornMain.DragonMetal(Str,Dex,Con,Int,Wis,Cha)
        Str = upgrade[0]
        Dex = upgrade[1]
        Con = upgrade[2]
        Int = upgrade[3]
        Wis = upgrade[4]
        Cha = upgrade[5]
        sub = 'Metallic'
        ele = upgrade[6]

    ele = DargonbornMain.setEle(ele)
    
elif(race==2):
    print ("Your race is: Dwarf\n")
elif(race==3):
    print ("Your race is: Elf")
elif(race==4):
    print ("Your race is: Gnome")
elif(race==5):
    print ("Your race is: Half-Elf")
elif(race==6):
    print ("Your race is: Halfling")
elif(race==7):
    print ("Your race is: Half-Orc")
elif(race==8):
    print ("Your race is: Human")
elif(race==9):
    print ("Your race is: Tiefling")
else:
    print("Invaild option:")
    race = (int(input("Enter the numeber for your Race: ")))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#class and level

menu = menuClass()
pri = printCharacter()

menu.printMenu()
clas = (int(input("Enter the numeber for your Class: ")))
print("\n\n")

#Error trap for menu class
while (clas<=0 or clas>=14):
    print("Invaild option:")
    clas = (int(input("Enter the number for your Class: \n\n")))

classNum = clas-1 #puts the input in a way that the program can find the class string

if(clas==1):
    menu.Artificer(clas)
    clas = menu.setclass(classHolder,classNum)
        
elif(clas==2):
    menu.Barbarian(clas)
    clas = menu.setclass(classHolder,classNum) #sets class to Barbarian string

elif(clas==3):
    menu.Bard(clas)
    clas = menu.setclass(classHolder,classNum) #sets class to Bard string
elif(clas==4):
    menu.Cleric(clas)
    clas = menu.setclass(classHolder,classNum) #sets class to Cleric string
elif(clas==5):
    print ("Your Class is: Druid")
elif(clas==6):
    print ("Your Class is: Fighter")
elif(clas==7):
    print ("Your Class is: Monk")
elif(clas==8):
    print ("Your Class is: Paladin")
elif(clas==9):
    print ("Your Class is: Ranger")
elif(clas==10):
    print ("Your Class is: Rouge")
elif(clas==11):
    print ("Your Class is: Sorcerer")
elif(clas==12):
    print ("Your Class is: Warlock")
elif(clas==13):
    print ("Your Class is: Wizard")
else:
    print("Invaild option:")
    clas = (int(input("Enter the numeber for your Class: ")))

levelup = input("Do you need to level up? ")
if (levelup[0].upper() == 'Y'):
    menu.Levelup(clas,lv)
else:
    print("you choose not to level up.")

display = (input("Would you like to see the information you choose? "))
if (display[0].upper() == 'Y'):
    pri.__repr__(name,clas,race,sub,lv,Str,Dex,Con,Int,Wis,Cha,ele)

    slowerprint("\n\nEnding Program...")
        
else:
    slowerprint("\n\nEnding Program...")

'''
answer = 'y'
while (answer == 'y' or answer == 'Y'):
    answer= input("Do you want correct your ____? ")
'''
