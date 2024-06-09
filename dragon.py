#Program runs successfully
import time
import random
from sys import exit

def game():
    print('\nYou are in the kindgdom of dragons. \nIn front of you, you see two caves. \nIn one cave the dragon is friendly and will share his tressure with you. \nThe other dragon is hungry and will eat you on sight')
    print()
    time.sleep(3)
    #The two outcomes that will happen inside the cave
    caveEvent1 = '\nA large dragon jumps out in front of you! \nHe opens his jaws and... \nGreets you and then gives his tressure!'
    caveEvent2 = '\nA large dragon jumps out in front of you! \nHe opens his jaws and... \nGobbles you down'
    #using random module
    eventSelect = [caveEvent1, caveEvent2]
    outcome = random.choices(eventSelect, k=1)
    #A while loop incase an invalid input is entered. it will be automatically looped if that is the case   
    cavenoLOOP = True 
    while cavenoLOOP == True:
        try:
            errorCheck = True #errorcheck will prevent the code from going through except: and finally: 
            caveno = int(input('To which cave will you go into? (1/2) '))
            if caveno == 1 or caveno == 2:
                time.sleep(2)
                print(outcome[0])
                time.sleep(2)
                cavenoLOOP = False
                errorCheck = False
                gameRestart()
            else:
                errorCheck = False
                print('\ninvalid selection!')
                print()
                time.sleep(1)
        except:
            if errorCheck == True:
                cavenoLOOP = True
                print('\nPlease enter either 1 or 2!')
                time.sleep(1)
        finally:
            if errorCheck == True:
                print() 

def gameRestart():
    #makes action based on player input
    def selection():
        playIN = str(input('\ndo you want to play again? (y/n) '))
        if playIN == 'y':
            game()
        elif playIN == 'n':
            exit()
        else:
            print('\ninvalid selection!!') #will retstart the function
            time.sleep(2)
            selection()
    selection() #calls the selection function 

#executing the main function
game()        


    
