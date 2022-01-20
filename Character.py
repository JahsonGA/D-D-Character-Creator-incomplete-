#Class: 
#Programer: Jahson Gonzalez-Allie
#Description: This class with collect information for a character sheet

from os import stat
import sys
import time
#slow print, prints slow
import random
#for dice roller

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./99999999999999999999999999999999999)# the larger the fraction is the slower it prints. set back to 10

def slowerprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)# the larger the fraction is the slower it prints

class diceroller():
    def stats():
        STAT = 6
        NUMDICE = 4
        x = 1
        y = 6
        gather=[0]*STAT    #creates 6 varables
        stat=[0]*NUMDICE   #creates 4 varables
        total = 0
        MIN = 0
        PLACEHOLDER = 0
        
        for i in range(0,STAT):    #rolls 6 times
            for j in range(0,NUMDICE):      #rolls 4d6 to one stat
                dice = random.randint(x,y)
                stat[j] = dice
            stat.sort() #puts the lowerest value at the front
            stat[0]=MIN   #sets smallest value to zero
            total = sum(stat)
            gather[i]=total
        gather.sort()
        return(gather)

    def asssign(stat):
        SIX = 6
        list = [0]*SIX
        remain = ['Str','Dex','Con','Int','Wis','Cha']      #for display
        options = []
        print(stat)
        
        for i in range(0,SIX):
            print("****************")
            print("1:Str\t    4:Int")
            print("2:Dex\t    5:Wis")
            print("3:Con\t    6:Cha")
            print("****************")
            print("Where do you want your stat",stat[i],":? ")
            x = int(input("Enter value from above: "))

            #error trap for x not in range
            while(x>=7 or x<=0):
                print("Invaild!!!")
                x = int(input("Enter value from above: "))

            #error trap for x already enter and out of range
            while(x in options):    
                print("You already assign that value to a stat!!!")
                x = int(input("Enter value from above: "))
                while(x>=7 or x<=0):
                    print("Invaild!!!")
                    x = int(input("Enter value from above: "))
                        
                

            print("")
            if(x==1):
                
                options.append(1)
                print("you choose Str")
                remain.remove('Str')
            elif(x==2):
                
                options.append(2)
                print("you choose Dex")
                remain.remove('Dex')
            elif(x==3):
                options.append(3)
                print("you choose Con")
                remain.remove('Con')
            elif(x==4):
                options.append(4)
                print("you choose Int")
                remain.remove('Int')
            if(x==5):
                options.append(5)
                print("you choose Wis")
                remain.remove('Wis')
            elif(x==6):
                options.append(6)
                print("you choose Cha")
                remain.remove('Cha')

            print("you still need",remain)
            print("")

            list[i]=x-1

        return(list)

class defaultCharacter():
    def __init__(self,name,clas,race,lv):
        self.name = name
        self.clas = clas
        self.race = race
        self.lv = lv

class setCharacter:
    def __init__(self,n1="blank",cl=[1,2,3,4,5,6,7,8,9,11,12,13],rc=[1,2,3,4,5,6,7,8,9],lv=0):
        self.name = n1
        self.clas = cl
        self.p2 = rc
        self.p3 = lv
#I dont know why this is needed


class menuClass():
    '''
    def __init__(self,x):
      # Ideally, self._options would be an empty dict for the base class.
      # This is just for the sake of example.
        self.options = {'1': self.Artificer,
                        '2': self.Barbarian,
                        '3': self.Bard,
                        '4': self.Cleric,
                        '5': self.Druid,
                        '6': self.Fighter,
                        '7': self.Monk,
                        '8': self.Paladin,
                        '9': self.Ranger,
                        '10': self.Rouge,
                        '11': self.Sorcerer,
                        '12': self.Warlock,
                        '13': self.Wizard}
        print(x)
    def handle_options(self, option):
        if option not in self.options:  #for whatever reason, this runs regurdless of option
            print ("Invalid option")
            # re-draw
            return
        self._options[option]()
    '''
    def printMenu(x):
        print("Please choose from the following options:\n \
                1:Artificer\t 2:Barbarian\t 3:Bard\t 4:Cleric\n \
                5:Druid\t 6:Fighter\t 7:Monk\t 8:Paladin\n \
                9:Ranger\t 10:Rouge\t 11:Sorcerer\t 12:Warlock\t 13:Wizard")

    def setclass(self,art, x):
        art = ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter\
            ', 'Monk', 'Paladin', 'Ranger', 'Rouge', 'Sorcerer', 'Warlock', 'Wizard']
        return art[x]

    def Artificer(self,x):
        slowprint("Your Class is: Artificer\n")
        slowprint("HIT POINTS")
        slowprint("Hit Dice: 1d8 per artificer level\nHit Points at 1st Level: 8 + your Constitution modifier\n \
        Hit Points at Higher Levels: 1d8 (or 5) + your Constitution modifier per artificer level after 1st\n")

        slowprint("Proficiencies")
        slowprint("Armor:           Light armor, medium armor, shields")
        slowprint("Weapons:         Simple weapons")
        slowprint("Tools:           Thieves' tools, tinker's tools, one type of artisan's tools of your choice")
        slowprint("Saving Throws:   Constitution, Intelligence")
        slowprint("Skills:          Choose two from Arcana, History, Investigation, Medicine, Nature, Perception, Sleight of Hand\n")

        slowprint("Equipment")
        slowprint("You start with the following equipment, in addition to the equipment granted by your background:")
        slowprint("\tany two simple weapons")
        slowprint("\ta light crossbow and 20 bolts")
        slowprint("\t(a) studded leather armor or (b) scale mail")
        slowprint("\tthieves' tools and a dungeoneer's pack\n")
        slowprint("Optional Rule: Firearm Proficiency")
        slowprint("The secrets of gunpowder weapons have been discovered in various corners of the D&D multiverse.\n\
    If your Dungeon Master uses the rules on firearms in the Dungeon Master's Guide and your artificer has been exposed\n\
    to the operation of such weapons, your artificer is proficient with them.")

    def Levelup(self,clas,lv): #x defual a null space
        file = clas
        type = '.txt'
        path = 'C:\\Users\\Owner\\.vscode\\Character Creator\\'
        filename = path+file+type
        ''' f = open(filename, "r").readlines()

        for y in range(lv+2):
            line = f[y]

            for y in range(1):
                header = len(y)

            for y in range(1,lv+1):
                body1 = len(y)

            if(header>= body1):
                lens = header

            for i in line.split(" "):
                print("{:<l%s}".format(i)%lens,end='')'''
        #Opens file based on filename
        with open(filename, 'r+') as file:

                #Manages line number and length_of_columns
                line_number = 1
                length_of_columns = []

                #For every line in the file
                for line in file:

                    #If it's the first line
                    if line_number == 1:

                        #Split (|) into headers list
                        headers = line.split('|')

                        #Removes new line character from last element
                        headers[-1] = headers[-1].split('\n')
                        headers[-1] = headers[-1][0]

                        #For every word in headers
                        for y in range(len(headers)):

                            #Add the length of the header as to the length of column
                            length_of_columns.append(len(headers[y]))
                        
                    #If it's the first line
                    if line_number != 1:

                        #Split the line as done previously
                        elements_in_line = line.split('|')
                        elements_in_line[-1] = elements_in_line[-1].split('\n')
                        elements_in_line[-1] = elements_in_line[-1][0]

                        #Sets column length based on lengthiest line
                        for z in range(len(elements_in_line)):
                            if len(elements_in_line[z]) > length_of_columns[z]:
                                length_of_columns[z] = len(elements_in_line[z])
                            z += 1
                            #Tracks line
                        line_number += 1

                #Reopens the file to use line if file
                with open(filename, 'r+') as file:
                    
                    #For line in file
                    for line in file:
                        
                        #Split (|) into line list
                        elements = line.split('|')

                        #Removes new line character
                        elements[-1] = elements[-1].split('\n')
                        elements[-1] = elements[-1][0]

                        #For every item in list 
                        for x in range(len(elements)):

                            #Gets spaces
                            spaces = length_of_columns[x] - len(elements[x]) + 3
                            tobeprinted = elements[x]

                            #For the descript column
                            if x == 2:
                                
                                #For the number of spaces needed
                                for y in range(spaces):

                                    #Creates element to be printed
                                    tobeprinted = tobeprinted + ' '

                            else:

                                #For the number of spaces needed/2
                                for z in range(int(spaces/2)):

                                    #Create a centered element
                                    tobeprinted = ' ' + tobeprinted + ' '
                                    
                            #Print without newline character
                            print(tobeprinted, end = '')

                        #Returns the line
                        print()
                
       

    def Barbarian(self,x):
        slowprint("Your Class is: Barbarian\n")
        slowprint("HIT POINTS")
        slowprint("Hit Dice: 1d12 per barbarian level\n \
        Hit Points at Higher Levels: 1d12 (or 7) + your Constitution modifier per barbarian level after 1st\n")

        slowprint("Proficiencies")
        slowprint("Armor:           Light armor, medium armor, shields")
        slowprint("Weapons:         Simple weapons, martial weapons")
        slowprint("Tools:           None")
        slowprint("Saving Throws:   Strength, Constitution")
        slowprint("Skills:          Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival\n")

        slowprint("Equipment")
        slowprint("You start with the following equipment, in addition to the equipment granted by your background:")
        slowprint("\t(a) a greataxe or (b) any martial melee weapon")
        slowprint("\t(a) two handaxes or (b) any simple weapon")
        slowprint("\tAn explorer's pack and four javelins")
        
        

    def Bard(self,x):
        print ("Your Class is: Bard\n")
        slowprint("Hit Dice: 1d8 per bard level")
        slowprint("Hit Points at 1st Level: 8 + your Constitution modifier")
        slowprint("Hit Points at Higher Levels: 1d8 (or 5) + your Constitution modifier per bard level after 1st")

        slowprint("Proficiencies")
        slowprint("Armor:           Light armor")
        slowprint("Weapons:         simple Weapons, hand crossbows, longswords, rapiers, shortswords")
        slowprint("Tools:           three Musical Instruments of your choice")
        slowprint("Saving Throws:   Dexterity, Charisma")
        slowprint("Skills:          Choose any three.\n")

        slowprint("Equipment")
        slowprint("You start with the following equipment, in addition to the equipment granted by your background:")
        slowprint("\t(a) a Rapier, (b) a Longsword, or (c) any simple weapon")
        slowprint("\t(a) a Diplomat's Pack or (b) an Entertainer's Pack")
        slowprint("\t(a) a lute or (b) any other musical instrument")
        slowprint("\tLeather Armor, and a Dagger")

    def Cleric(self,x):
        print ("Your Class is: Cleric\n")
        slowprint("Hit Dice: 1d8 per Cleric level")
        slowprint("Hit Points at 1st Level: 8 + your Constitution modifier")
        slowprint("Hit Points at Higher Levels: 1d8 (or 5) + your Constitution modifier per bard level after 1st")

        slowprint("Proficiencies")
        slowprint("Armor:           Light Armor, Medium Armor, Shields")
        slowprint("Weapons:         simple Weapons")
        slowprint("Tools:           none")
        slowprint("Saving Throws:   Wisdom, Charisma")
        slowprint("Skills:          Choose two from History, Insight, Medicine, Persuasion, and Religion\n")

        slowprint("Equipment")
        slowprint("You start with the following equipment, in addition to the equipment granted by your background:")
        slowprint("\t(a) a mace or (b) a Warhammer (if proficient)")
        slowprint("\t(a) Scale Mail, (b) Leather Armor, or (c) Chain Mail (if proficient)")
        slowprint("\t(a) a Light Crossbow and 20 bolts or (b) any simple weapon")
        slowprint("\t(a) a Priest's Pack or (b) an Explorer's Pack")
        slowprint("\tA Shield and a holy Symbol")
    def Druid(self,x):
        print ("Your Class is: Druid")

    def Fighter(self,x):
        print ("Your Class is: Fighter")

    def Monk(self,x):
        print ("Your Class is: Monk")

    def Paladin(self,x):
        print ("Your Class is: Paladin")

    def Ranger(self,x):
        print ("Your Class is: Ranger")

    def Rouge(self,x):
        print ("Your Class is: Rouge")

    def Sorcerer(self,x):
        print ("Your Class is: Sorcerer")

    def Warlock(self,x):
        print ("Your Class is: Warlock")

    def Wizard(self,x):
        print ("Your Class is: Wizard")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#Races

class RaceClass:

    def menuRace():
        print("Please choose from the following options:\n \
                1:Dragonborn\t 2:Dwarf\t 3:Elf\t\t 4:Gnome\n \
                5:Half-Elf\t 6:Halfling\t 7:Half-Orc\t 8:Human\n \
                9:Tiefling")

    def setrace(art, x):
        art = ['Dragonborn','Dwarf','Elf','Gnome','Half-Elf','Halfling','Half-Orc','Human','Tiefling']
        return art[x]

class printCharacter():
    def __repr__ (self,name,clas,race,sub,lv,Str,Dex,Con,Int,Wis,Cha,ele):

        name_str = "Name:",name
        class_str = "Class:",clas
        race_str = "Race:",sub,race
        level_str = "Level:",lv

        print("********************************************************")
        print(name_str,class_str)
        print(race_str,level_str)
        print("********************************************************")
        print("Str: ",Str)
        print("Dex: ",Dex)
        print("Con: ",Con)
        print("Int: ",Int)
        print("Wis: ",Wis)
        print("Cha: ",Cha)
        if(race == "Dragonborn"):
            print("\nSpeed: 30")
            print("Languages. You can read, speak, and write Common and Draconic.")
            slowprint("""\n\nBreath Weapon. You can use your action to exhale destructive energy. 
It deals damage in an area according to your ancestry. When you use your breath weapon, 
all creatures in the area must make a saving throw, the type of which is determined by your ancestry.
The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. 
A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. 
The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. 
After using your breath weapon, you cannot use it again until you complete a short or long rest.""")
            print("\nBreath weapon:",ele[1],ele[2]) #prints the damage type and area of effect of breath weapon
            if(sub == 'Standard'):
                print("Dragon born",ele[1]) #prints the type of dragonborn
            elif(sub == 'Draconblood'):
                print("Dragon born",ele[1])
                print("Forceful Presence: Intimidation or Persuasion check, you can do so with advantage once per long rest.")
            elif(sub == 'Ravenite'):
                print("Dragonborn",ele[1])
                print("Vengeful Assault: When you take damage from a creature in range of a weapon you are wielding,\
you can use your reaction to make an attack against that creature. You can do this once per short or long rest.")
            elif(sub == "Chromatic"):
                print("Chromatic Warding: starting at 5th level, as an action, you can channel \
your draconic energy to protect yourself. for 1 minute, you become immune to",ele[1])
                print("once you use this trait, you con't do so again until you finished a long rest")
            elif(sub == "Gem"):
                slowprint("""Psionic Mind. \n\tYou can telepathically speak to any creature you can see within 30 feet of you.
You don't need to share a language with the creature, but the creature must be able to understand at least one language.
Gem Flight.\n\t Starting at 5th level, you can use a bonus action to manifest spectral wings on your body. 
These wings last for 1 minute. For the duration, you gain a flying speed equal to your walking speed and can hover.""")
                print("Once you use this trait, you can't do so again until you finish a long rest.")
            elif(sub == "Metallic"):
                slowprint("\tMetallic Breath Weapon. At 5th level, you gain a second breath weapon.")
                slowprint("When you take the Attack action on your turn, you can replace one of your attacks with an exhalation in a 15-foot cone.")
                slowprint("The save DC for this breath is 8 + your Constitution modifier + your proficiency bonus. Whenever you use this trait, choose one:")
                slowprint("""\t\tEnervating Breath. Each creature in the cone must succeed on a Constitution saving throw 
or become incapacitated until the start of your next turn.""")
                slowprint("""\n\t\tRepulsion Breath. Each creature in the cone must succeed on a Strength saving throw or 
be pushed 20 feet away from you and be knocked prone.""")
                print("Once you use your Metallic Breath Weapon, you can't do so again until you finish a long rest.")
        else:
            print("working on it")
