


from os import stat
import sys
import time
from turtle import speed

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./99999999999999999999999999999999999)# the larger the fraction is the slower it prints. set back to 10


class DargonbornMain():

    def dragonBorn(sub):
        age = "Age:\n\t Young dragonborn grow quickly.\
They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3,\
and reach adulthood by 15. They live to be around 80.\n"
        alignment = "Alignment:\n\t Dragonborn tend towards extremes, making a conscious choice for one side or the other between Good and Evil\
(represented by Bahamut and Tiamat,respectively). More side with Bahamut than Tiamat (whose non-dragon followers are mostly kobolds),\
but villainous dragonborn can be quite terrible indeed. Some rare few choose to devote themselves to lesser dragon deities, such as Chronepsis (Neutral),\
and fewer still choose to worship Io, the Ninefold Dragon, who is all alignments at once.\n"
        size = "Size:\n\t Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds.\
Your size is Medium.\n"
        speed = "Speed:\n\t Your base walking speed is 30 feet.\n"
        Draconic_Ancestry="Draconic Ancestry. You are distantly related to a particular kind of dragon.\
You will be asked to choose a type of dragon from the below list; this determines the damage and area of your breath weapon,\
and the type of resistance you gain.\n"
        languages = "Languages:\n\t You can read, speak, and write Common and Draconic."
        breathweapon = "\nBreath Weapon:\n\t You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. \
When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry.\
The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus.\
A creature takes 2d6 damage on a failed save, and half as much damage on a successful one.\
The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level.\
After using your breath weapon, you cannot use it again until you complete a short or long rest."

        slowprint("You choice Dragonborn\n")
        slowprint(age)
        slowprint(alignment)  
        slowprint(size)
        slowprint(speed)
        slowprint(Draconic_Ancestry)
        slowprint(languages)
        slowprint(breathweapon)
        print("Please choose your subrace")
        print("********************************")
        print("1:Standard\t4:Chromatic ")
        print("2:Draconblood\t5:Gem ")
        print("3:Ravenite\t6:Metallic ")
        print("********************************")
        sub = int(input("Enter value from above: "))

        #error trap for x not in range
        while(sub>=7 or sub<=0):
            print("Invaild!!!")
            sub = int(input("Enter value from above: "))
        return(sub)

    def setEle(ele):
        ele = int(ele)
        dic = {
                1:["Black","Acid","5' by 30' line (DEX save)"],
                2:["Blue","Lightning","5' by 30' line (DEX save)"],
                3:["Brass","Fire","5' by 30' line (DEX save)"],
                4:["Bronze","Lightning","5' by 30' line (DEX save)"],
                5:["Copper","Acid","5' by 30' line (DEX save)"],
                6:["Gold","Fire","15' cone (DEX save)"],
                7:["Green","Poison","15' cone (CON save)"],
                8:["Red",'Fire',"15' cone (CON save)"],
                9:["Silver","Cold","15' cone (CON save)"],
                10:["White","Cold","15' cone (CON save)"],
                11:["Amethyst","Force","15' cone (DEX save)"],
                12:["Crystal","Radiant","15' cone (DEX save)"],
                13:["Emerald","Psychic","15' cone (DEX save)"],
                14:["Sapphire","Thunder","15' cone (DEX save)"],
                15:["Topaz","Necrotic","15' cone (DEX save)"],
            }

        return(dic[ele])

    def DragonbornStandard(Str,Cha):
        ele = 0 #element off the standard dragonborn
        print("Dragon Color   Damage Type   Breath Weapon")
        print("")
        print("1.Black        Acid          5' by 30' line (DEX save)")
        print("2.Blue         Lightning     5' by 30' line (DEX save)")
        print("3.Brass        Fire          5' by 30' line (DEX save)")
        print("4.Bronze       Lightning     5' by 30' line (DEX save)")
        print("5.Copper       Acid          5' by 30' line (DEX save)")
        print("6.Gold         Fire          15' cone (DEX save)")
        print("7.Green        Poison        15' cone (CON save)")
        print("8.Red          Fire          15' cone (DEX save)")
        print("9.Silver       Cold          15' cone (CON save)")
        print("10.White       Cold          15' cone (CON save)")
        ele = input("Enter the color of your scales: ")

        while (ele<=0 or ele>=11):
            print("Invaild")
            ele = input("Enter the color of your scales: ")

        upgrade = [Str+2,Cha+1, ele]
        return(upgrade)

    def DragonbornBlood(Int,Cha):
        ele = 0 #element of draconblood dragonborn
        print("Dragon Color   Damage Type   Breath Weapon")
        print("")
        print("1.Black        Acid          5' by 30' line (DEX save)")
        print("2.Blue         Lightning     5' by 30' line (DEX save)")
        print("3.Brass        Fire          5' by 30' line (DEX save)")
        print("4.Bronze       Lightning     5' by 30' line (DEX save)")
        print("5.Copper       Acid          5' by 30' line (DEX save)")
        print("6.Gold         Fire          15' cone (DEX save)")
        print("7.Green        Poison        15' cone (CON save)")
        print("8.Red          Fire          15' cone (DEX save)")
        print("9.Silver       Cold          15' cone (CON save)")
        print("10.White       Cold          15' cone (CON save)")
        ele = input("Enter the color of your scales: ")

        while (ele<=0 or ele>=11):
            print("Invaild")
            ele = input("Enter the color of your scales: ")

        upgrade = [Int+2,Cha+1, ele]
        return(upgrade)

    def DragonbornRavenite(Str,Con):
        ele = 0 #element of Ravenite dragonborn
        print("Dragon Color   Damage Type   Breath Weapon")
        print("")
        print("1.Black        Acid          5' by 30' line (DEX save)")
        print("2.Blue         Lightning     5' by 30' line (DEX save)")
        print("3.Brass        Fire          5' by 30' line (DEX save)")
        print("4.Bronze       Lightning     5' by 30' line (DEX save)")
        print("5.Copper       Acid          5' by 30' line (DEX save)")
        print("6.Gold         Fire          15' cone (DEX save)")
        print("7.Green        Poison        15' cone (CON save)")
        print("8.Red          Fire          15' cone (DEX save)")
        print("9.Silver       Cold          15' cone (CON save)")
        print("10.White       Cold          15' cone (CON save)")
        ele = input("Enter the color of your scales: ")

        while (ele<=0 or ele>=11):
            print("Invaild")
            ele = input("Enter the color of your scales: ")

        upgrade = [Str+2,Con+1,ele]
        return(upgrade)

    def DragonChromatic(Str,Dex,Con,Int,Wis,Cha):
        count = 0
        ele = 0 #element of Chromatic Dragonborn

        print("Dragon Color   Damage Type   Breath Weapon")
        print("")
        print("1.Black        Acid          5' by 30' line (DEX save)")
        print("2.Blue         Lightning     5' by 30' line (DEX save)")
        print("3.Green        Poison        15' cone (CON save)")
        print("4.Red          Fire          15' cone (DEX save)")
        print("5.White       Cold          15' cone (CON save)")
        ele = int(input("Enter the color of your scales: "))

        while (ele<=0 or ele>=11):
            print("Invaild")
            ele = input("Enter the color of your scales: ")

        if (ele==1):
            pass
        elif (ele==2):
            pass
        elif (ele==3):
            ele+=4  #the marked score is 7 so add 4 to the display value
        elif (ele==4):
            ele+=4  #the marked score is 8 so add 4 to the display value
        elif (ele==5):
            ele+=5  #the marked score is 10 so add 5 to the display value


        upgrade = [Str,Dex,Con,Int,Wis,Cha, ele]


        while(count != 3):
            print("****************")
            print("1:Str\t    4:Int")
            print("2:Dex\t    5:Wis")
            print("3:Con\t    6:Cha")
            print("****************")
            print("What stat do you want to increase +1:? ")
            x = int(input("Enter value from above: "))

            #error trap for x not in range
            while(x>=7 or x<=0):
                print("Invaild!!!")
                x = int(input("Enter value from above: "))

            if(x==1):    
                print("Increasing your Str stat")
                upgrade[0]=upgrade[0]+1
                print("new score",upgrade[0])
            elif(x==2):
                print("Increasing your Dex stat")
                upgrade[1]=upgrade[1]+1
                print("new score",upgrade[1])
            elif(x==3):
                print("Increasing your Con stat")
                upgrade[2]=upgrade[2]+1
                print("new score",upgrade[2])
            elif(x==4):
                print("Increasing your Int stat")
                upgrade[3]=upgrade[3]+1
                print("new score",upgrade[3])
            elif(x==5):
                print("Increasing your Wis stat")
                upgrade[4]=upgrade[4]+1
                print("new score",upgrade[4])
            elif(x==6):
                print("Increasing your Cha stat")
                upgrade[5]=upgrade[5]+1
                print("new score",upgrade[5])
            else:
                print("Chromatic Dragonborn ERROR")
            count += 1

        return(upgrade)



    def DragonGem(Str,Dex,Con,Int,Wis,Cha):
        ele = 0 #element fo Gem Dragonborn
        count = 0
        print("Dragon Color   Damage Type   Breath Weapon\n")

        print("1.Amethyst    Force         15' cone (DEX save)")
        print("2.Crystal     Radiant       15' cone (DEX save)")
        print("3.Emerald     Psychic       15' cone (DEX save)")
        print("4.Sapphire    Thunder       15' cone (DEX save)")
        print("5.Topaz       Necrotic      15' cone (DEX save)")
        ele = int(input("Enter the color of your scales: "))

        while (ele<=0 or ele>=6):
            print("Invaild")
            ele = input("Enter the color of your scales: ")

        if (ele==1):
            ele+=10  #the marked score is 1 so add 10 to the display value
        elif (ele==2):
            ele+=10  #the marked score is 2 so add 10 to the display value
        elif (ele==3):
            ele+=10  #the marked score is 3 so add 10 to the display value
        elif (ele==4):
            ele+=10  #the marked score is 4 so add 10 to the display value
        elif (ele==5):
            ele+=10  #the marked score is 5 so add 10 to the display value

        upgrade = [Str,Dex,Con,Int,Wis,Cha,ele]

        while(count != 3):
            print("****************")
            print("1:Str\t    4:Int")
            print("2:Dex\t    5:Wis")
            print("3:Con\t    6:Cha")
            print("****************")
            print("What stat do you want to increase +1:? ")
            x = int(input("Enter value from above: "))

            #error trap for x not in range
            while(x>=7 or x<=0):
                print("Invaild!!!")
                x = int(input("Enter value from above: "))
            

            if(x==1):    
                print("Increasing your Str stat")
                upgrade[0]=upgrade[0]+1
                print("new score",upgrade[0])
            elif(x==2):
                print("Increasing your Dex stat")
                upgrade[1]=upgrade[1]+1
                print("new score",upgrade[1])
            elif(x==3):
                print("Increasing your Con stat")
                upgrade[2]=upgrade[2]+1
                print("new score",upgrade[2])
            elif(x==4):
                print("Increasing your Int stat")
                upgrade[3]=upgrade[3]+1
                print("new score",upgrade[3])
            elif(x==5):
                print("Increasing your Wis stat")
                upgrade[4]=upgrade[4]+1
                print("new score",upgrade[4])
            elif(x==6):
                print("Increasing your Cha stat")
                upgrade[5]=upgrade[5]+1
                print("new score",upgrade[5])
            else:
                print("DragonGem upgrade ERROR")          
            count += 1

        return(upgrade)

    def DragonMetal(Str,Dex,Con,Int,Wis,Cha):
        ele = 0 #element of Metallic dragonborn
        count = 0

        print("Dragon Color   Damage Type   Breath Weapon")
        print("")
        print("1.Brass        Fire          5' by 30' line (DEX save)")
        print("2.Bronze       Lightning     5' by 30' line (DEX save)")
        print("3.Copper       Acid          5' by 30' line (DEX save)")
        print("4.Gold         Fire          15' cone (DEX save)")
        print("5.Silver       Cold          15' cone (CON save)")
        ele = int(input("Enter the color of your scales: "))

        while (ele<=0 or ele>=6):
            print("Invaild")
            ele = int(input("Enter the color of your scales: "))


        if (ele==1):
            ele+=2  #the marked score is 1 so add 2 to the display value
        elif (ele==2):
            ele+=2  #the marked score is 2 so add 2 to the display value
        elif (ele==3):
            ele+=2  #the marked score is 3 so add 2 to the display value
        elif (ele==4):
            ele+=2  #the marked score is 4 so add 2 to the display value
        elif (ele==5):
            ele+=4  #the marked score is 5 so add 4 to the display value

        upgrade = [Str,Dex,Con,Int,Wis,Cha,ele]


        while(count != 3):
            print("****************")
            print("1:Str\t    4:Int")
            print("2:Dex\t    5:Wis")
            print("3:Con\t    6:Cha")
            print("****************")
            print("What stat do you want to increase +1:? ")
            x = int(input("Enter value from above: "))

            #error trap for x not in range
            while(x>=7 or x<=0):
                print("Invaild!!!")
                x = int(input("Enter value from above: "))

            if(x==1):    
                print("Increasing your Str stat")
                upgrade[0]=upgrade[0]+1
                print("new score",upgrade[0])
            elif(x==2):
                print("Increasing your Dex stat")
                upgrade[1]=upgrade[1]+1
                print("new score",upgrade[1])
            elif(x==3):
                print("Increasing your Con stat")
                upgrade[2]=upgrade[2]+1
                print("new score",upgrade[2])
            elif(x==4):
                print("Increasing your Int stat")
                upgrade[3]=upgrade[3]+1
                print("new score",upgrade[3])
            elif(x==5):
                print("Increasing your Wis stat")
                upgrade[4]=upgrade[4]+1
                print("new score",upgrade[4])
            elif(x==6):
                print("Increasing your Cha stat")
                upgrade[5]=upgrade[5]+1
                print("new score",upgrade[5])
            else:
                print("Metallic Dragonbor ERROER")
            count += 1

        return(upgrade)
