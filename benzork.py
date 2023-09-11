import pygame
import random
import time
from pygame.locals import *

pygame.init()



intro = '''   Hello, welcome to Pyork! Yes I understand it is a bit of a stretch but
                      don't you worry, it's super fun!
      All you need to remember is that the words are not case-sensitive
                and you don't need punctuation marks, ie:( . , ? ! )
                                    HAVE FUN!!!
                                    
      ps... If you want to see the Pyork Documention, type "pydoc" while in the       field


   You wake up in the middle of a field, alone. You have a pounding in your head and you can't remember a thing. You don't know who you are or how you got here. It is pitch-black night but, luckily, there is a full moon out. There is a\npath leading to the north and another to the east.'''

items = []

print(intro)
print()







# 1: field (in play; needs more general reponses)

# 2: yard (in play; needs more general reponses)

# 3: yardr (in play; needs more general reponses)

# 4: barn (in play; needs more general reponses)

# 5: inbarn (in play; needs more general reponses)

# 6: loft (in play; needs more general reponses)

# 7: shed (in play; needs more general reponses)

# 8: inshed (in play; needs more general responses)

# 9: fronthouse (in play; needs more general reponses)

# 10: livingroom (in play; needs more general reponses)

# 11: kitchen (in play; needs more general reponses)

# 12: hall (in play; needs more general reponses)

# 13: bathroom (in play; needs more general reponses)

# 14: bedroom (in play; needs more general reponses)

# 15: study (in play; needs more general reponses)



# 16: truck (in play; needs more general reponses)

# 17: river (in play; needs more general reponses)

# 18: pond (in play; needs more general reponses)

# 19: island (in play; needs more general reponses)

# 20: islandwoods (in play; needs more general reponses)








MAP = '''

______________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|       _____                                | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |   \                          |
| |B| |_house_|  \ |                         |
|    yard        | |                         | 
|    ||          | |                         |
| ___||___      / / ___                      |   
| |field |     / /  |S|                      |
| |      |____/ /                            |
| |___________/                              |
|____________________________________________|

'''


MAPA = '''

______________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|                                            | 
|                                            |
|                                            |   
|                                            |
|                                            |
|                                            | 
|    ||                                      |
| ___||___                                   |   
| |field |                                   |
| |      |_____                              |
| |____________                              |
|____________________________________________|

'''

MAPB = '''

______________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|       _____                                | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |                              |
| |B| |_house_|                              |
|    yard                                    | 
|    ||                                      |
| ___||___                                   |   
| |field |                                   |
| |      |____                               |
| |___________                               |
|____________________________________________|

'''

MAPC = '''

______________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|                                            | 
|                                            |
|                                            |   
|                 \                          |
|                \ |                         |
|                | |                         | 
|    ||          | |                         |
| ___||___      / / ___                      |   
| |field |     / /  |S|                      |
| |      |____/ /                            |
| |____________/                             |
|____________________________________________|

'''

MAPD = '''

_____________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|       _____                                | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |   \                          |
| |B| |_house_|  \ |                         |
|    yard        | |                         | 
|    ||          | |                         |
| ___||___      / / ___                      |   
| |field |     / /  |S|                      |
| |      |____/ /                            |
| |___________/                              |
|____________________________________________|

'''

MAPFRONTOFHOUSE = '''

_____________________________________________
|         ||                                 |
|         ||                         ________|
|         ||  __    _____           / _______|
|            {  }   ____ \_________/ /       | 
|       _____[__]       \___________/        | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |   \                          |
| |B| |_house_|  \ |                         |
|    yard        | |                         | 
|    ||          | |                         |
| ___||___      / / ___                      |   
| |field |     / /  |S|                      |
| |      |____/ /                            |
| |____________/                             |
|____________________________________________|

'''

MAPFRONTOFHOUSENOEAST = '''

_____________________________________________
|         ||                                 |
|         ||                         ________|
|         ||  __    _____           / _______|
|            {  }   ____ \_________/ /       | 
|       _____[__]       \___________/        | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |                              |
| |B| |_house_|                              |
|    yard                                    | 
|    ||                                      |
| ___||___                                   |   
| |field |                                   |
| |      |____                               |
| |____________                              |
|____________________________________________|

'''


MAPFRONTOFHOUSENOBARN = '''

_____________________________________________
|         ||                                 |
|         ||                         ________|
|         ||  __    _____           / _______|
|            {  }   ____ \_________/ /       | 
|       _____[__]       \___________/        | 
|      /     \                               |
|     / [] [] \                              |   
|     |       |   \                          |
|     |_house_|  \ |                         |
|                | |                         | 
|    ||          | |                         |
| ___||___      / / ___                      |   
| |field |     / /  |S|                      |
| |      |____/ /                            |
| |____________/                             |
|____________________________________________|

'''

YRMAP1 = '''

______________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|       _____                                | 
|      /     \                               |
|     / [] [] \                              |   
|     |       |   \                          |
|     |_house_|  \ |                         |
|                | |                         | 
|    ||          | |                         |
| ___||___      / / ___                      |   
| |field |     / /  |S|                      |
| |      |____/ /                            |
| |___________/                              |
|____________________________________________|

'''


YRMAP2 = '''

______________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|       _____                                | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |                              |
| |B| |_house_|                              |
|    yard                                    | 
|    ||                                      |
| ___||___                                   |   
| |field |                                   |
| |      |____                               |
| |___________                               |
|____________________________________________|

'''





MAPOFPONDTRUCK = '''

_____________________________________________
|         ||                                 |
|         ||                         ________|
|         ||  __    _____           / _______|
|            {  }   ____ \_________/ /       | 
|       _____[__]       \___________/        | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |   \                          |
| |B| |_house_|  \ |                         |
|    yard        | |                         | 
|    ||          | |                         |
| ___||___      / / ___ ____                 |   
| |field |     / /  |S| ___ \_       ________|
| |      |____/ /          \__      |      __|
| |____________/                    |     |  | <--island
|                               <()>|     |__|
|                                    \_______|
|                                      pond  |
|____________________________________________|

'''



MAPOFPONDNOTRUCK = '''

______________________________________________
|                                            |
|                                            |
|                                            |
|                                            | 
|       _____                                | 
|      /     \                               |
|     / [] [] \                              |   
| ___ |       |   \                          |
| |B| |_house_|  \ |                         |
|    yard        | |                         | 
|    ||          | |                         |
| ___||___      / / ___ ____                 |   
| |field |     / /  |S| ___ \_       ________|
| |      |____/ /          \__      |      __|
| |___________/                     |     |  | <--island
|                               <()>|     |__|
|                                    \_______|
|                                      pond  |
|____________________________________________|

'''

MAPOFRIVER = '''
  
______________________________________________                                             
|                                             |  
|           (*)(*) (*)(*) (*)(*) (*) (*) (*)  |  
|        (*) |  |   |  |   |  |   |   |   |   | 
|         |  (*)(*)(*)  (*) (*)(*) (*)(*) (*) |   
|(*)    (*)(*)|  |  |    |   |  |   |  |   |  |   
| |      |  |(*)(*) (*)(*)(*) (*)(*) (*)(*)(*)|  
|(*)   (*)(*) |  |   |  |  |   |  |   |  |  | |
| |     |  |  ________________________________|                                 
|____________/    ~~     ~~~   ~~~     ~~ ~~~ |                       
| ~~         ~~~   ~~     ~~     ~~~~   ~     |             
|~~ ~~~ ~~~~     ~~   ~~~~~  ~~   ~~~~   ~~~  |                            
| ~~   ~~   ~~ _______________________________|
|_____________/                               |             
|    /   \     (*)(*) (*)(*)  (*)(*)(*) (*)(*)|                          
|               |  |   |  |    |  |  |   |  | |          
|       <()>  (*)(*)(*)(*)(*)(*) (*)(*) (*)(*)|                 
|    ||        |  |  |  |  |  |   |  |   |  | |               
|    ||        (*)(*)(*)  (*)(*)(*)  (*)(*)   |                           
|____||_________|__|__|____|_ |__|____|__|____|

'''

HALLBEDROOM = '''
                ________________________________________________
                |                                               |
                |                                               |
                |                                               |
                |                                               |
                |                _D_                            |
                |                | |                            |
                |       ________ | |                            |
                |      |           |D                           |
                |      |  BED   || |                            |       
                |      |________|| |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''


HALLBEDSTUDY = '''
                ________________________________________________
                |                                               |
                |                                               |
                |                                               |
                |                                               |
                |                _D_                            |
                |                | |   _______                  |
                |       ________ | |__| study |                 |
                |      |            __        |                 |
                |      |  BED   || |  |_______|                 |       
                |      |________|| |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''

HALLBATHROOM = '''
                ________________________________________________
                |                                               |
                |                                               |
                |              ________                         |
                |              | BATH |                         |
                |              |_  ___|                         |
                |                | |                            |
                |                | |                            |
                |                | |D                           |
                |               D| |                            |       
                |                | |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''

HALLBATHBED = '''
                ________________________________________________
                |                                               |
                |                                               |
                |              ________                         |
                |              | BATH |                         |
                |              |_  ___|                         |
                |                | |                            |
                |       ________ | |                            |
                |      |           |D                           |
                |      |  BED   || |                            |       
                |      |________|| |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''

HALLALL = '''
                ________________________________________________
                |                                               |
                |                                               |
                |              ________                         |
                |              | BATH |                         |
                |              |_  ___|                         |
                |                | |   _______                  |
                |       ________ | |__| study |                 |
                |      |            __        |                 |
                |      |  BED   || |  |_______|                 |       
                |      |________|| |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''

HALLSTUDYBATH = '''
                ________________________________________________
                |                                               |
                |                                               |
                |              ________                         |
                |              | BATH |                         |
                |              |_  ___|                         |
                |                | |   _______                  |
                |                | |__| study |                 |
                |                | |__        |                 |
                |               D| |  |_______|                 |       
                |                | |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''

HALLSTUDY = '''
                ________________________________________________
                |                                               |
                |                                               |
                |                                               |
                |                                               |
                |                _D_                            |
                |                | |   _______                  |
                |                | |__| study |                 |
                |                | |__        |                 |
                |               D| |  |_______|                 |       
                |                | |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''

HALLBLANK = '''
                ________________________________________________
                |                                               |
                |                                               |
                |                                               |
                |                                               |
                |                _D_                            |
                |                | |                            |
                |                | |                            |
                |                | |D                           |
                |               D| |                            |       
                |                | |                            |
                |                | |                            |
                |-----------------------------------------------|

                '''


barnnote = '''

        April 19, 2010

           I have been forced to stay in this barn for the past 2 days
        because I cannot find a way into the house. My rations are getting
        low and I will soon have to find some more. I can\'t sleep at night
        because of this awful howling I keep hearing in the distance to the east.
        I pray every night it doesn\'t get any closer but it seems it is. I\'m
        exhausted and restless at the same time. I haven\'t gone out much because
        of the howling, but I am going to have to soon. If anyone finds this note,
        my name is Daniel Crosby. I lived in Sandusky, Ohio before all of this. I
        was an accountant. Tell Trish Crosby I love her.'''
                            




def main():
           
        global mapb     
        global door
        global machete
        global mapc
        global arm
        global eastopen
        global memory1
        global lrmap
        global mapfront
        global exarm
        global inshedmemory
        global playedpiano
        global mapofpond
        global rightofhouse
        global toolchoice
        global moves
        global lookedattable
        global ovenopened
        global microwaveopened
        global fridgeopened
        global boatplug
        global boatplugriver
        global foundman
        global checkonman
        global dead
        global mightbedead
        global notdead 
        global bathroommap
        global bedroommap
        global studymap
        global shower
        global brokeglass
        global turnedover
        global deadinfield
        global deadinfronthouse
        global deadinpond
        global deadinriver
            





##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################




        
# 0: place = ['field']-------------------------------------------------------------------------------------------------------------------------------------------

        global place
        
        if place == ['field']:
                
                
    
            global mapa
            mapa = 1
            
                    
                    
            
            
            greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in the middle of a field. It is some time at\nnight and you see that there is a full moon out. There is a trail to\nthe north and a trail to the east.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }
            field = 1

            while field == 1:
                    
                    if mightbedead == 1:
                            randomattack == random.randint(1,10)
                            if randomattack == 1:
                                    print('Oh no! The man with the severed arm is back!')
                                    print('press enter')
                                    input()
                                    print('What are you going to do?')
                                    whattodo = input('"run" or "fight"')
                                    if whattodo == 'run':
                                            rand = random.randint(1,2)
                                            if rand == 1:
                                                    print('The man runs after you but slips on an ear of corn, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('As he falls the man lunges forward and lands directly on his neck.')
                                                    print('press enter')
                                                    input()
                                                    print('There is no need to check again or to double tap. The man is very dead.')
                                                    print()
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinfield = 1
                                            else:
                                                    print('The man runs after you but slips on an ear of corn, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('The man falls directly on his face and is stunned.')
                                                    print('press enter')
                                                    input()
                                                    print('You seize the opportunity and quickly jump up and down on his head, flattening him into the ground. The man is very dead now. Good job.')
                                                    print()    
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinfield = 1

                                    elif whattodo == 'fight':
                                            random = random.randint(1,2)
                                            if random == 1:
                                                    print('You start to think which weapon you are going to use but there is no time; the man lunges forward.')
                                                    print('press enter')
                                                    input()
                                                    print('You dodge and land a punch square on his jaw, causing him to reel backward and fall over.')
                                                    print('press enter')
                                                    input()
                                                    print('HA! What a bit of luck. It seems the man has fallen onto an up-turn pitchfork. It has impaled the man in the chest and he is dying.')
                                                    print('press enter')
                                                    input()
                                                    print('You step on his chest making the spikes penetrate deeper into the mans body. He has died.')
                                                    print()
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinfield = 1
                                            else:
                                                   print('You start to think which weapon you are going to use but there is not time; the man leaps forward.')
                                                   print('press enter')
                                                   input()
                                                   print('You try to dodge but he lands on top of you pinning you down growling and drooling in your face.')
                                                   print('press enter')
                                                   input()
                                                   print('You must decide now! Between two options: option "1" or option "2"')
                                                   oneortwo = input('"1" or "2"')
                                                   if oneortwo == '1':
                                                           print('I\'m so sorry, but your attempt to break free has ended up with the man sinking his teeth into your neck and pulling. You are quite dead. Sorry.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           field = 0
                                                           
                                                   elif oneortwo == 2:
                                                           print('Yes! Your barrel roll sends the man flying off of you and back into the woods.')
                                                           print('You cannot see him but you hear his footsteps getting more and more distant.')
                                                           print()

                                                   else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           field = 0

                                                           
                                    else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           field = 0
                                            
                    else:
                            None

                                                    
                    print('Field')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      field = 0
                      global running
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()
                                          

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()
                            
                    elif start == 'pydoc':
                            print(PYDOC)
                            print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()                
                                            

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                                            
                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()                

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                                            
                                                    


                    elif start == 'go to barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    field = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                    elif start == 'barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    field = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                      
                      
                    elif start == 'go to shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    field = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()

                    elif start == 'shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    field = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()
                     
                      

                    elif start == 'go to house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    field = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()
                                   
                    elif start == 'house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    field = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()





                    elif start == 'go to the house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    field = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
                            

                                    
                      
                    elif start == 'north':
                            print('You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.')
                            print()
                            
                            place = ['yard']
                            field = 0
                            mapb = 1

                    elif start == 'go north':
                            print('You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.')
                            print()
                            place = ['yard']
                            field = 0
                            mapb = 1
                     

                                   
                        
                        
                     
                        
                
                        
                    
                        
                        

                                   
                        
                    
                    elif start == 'east':
                            if arm == 1:
                                    print('You walk out from the field and come upon an old shed. There is a trail leading north and one leading south back to the field.')
                                    print()
                                    place = ['shed']
                                    mapc = 1
                                    field = 0
                            else:
                                    
                                print('You walk out from the field and come upon an old shed. There is a trail leading north. There is also an object being illuminated by the moon on the ground next to the shed. What is that!')
                                print()
                        
                                place = ['shed']
                                mapc = 1
                                field = 0

                    elif start == 'go east':
                       if arm == 1:
                                    print('You walk out from the field and come upon an old shed. There is a trail leading north and one leading south back to the field.')
                                    print()
                                    place = ['shed']
                                    mapc = 1
                                    field = 0
                       else:
                                    
                                print('You walk out from the field and come upon an old shed. There is a trail leading north. There is also an object being illuminated by the moon on the ground next to the shed. What is that!')
                                print()
                        
                                place = ['shed']
                                mapc = 1
                                field = 0
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'take corn':
                         
                         items.append('corn')
                      
                         print('Corn taken.')
                         print()

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print(greet['jump'])
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                     if deadinfield == 0:
                             
                      print(greet['la'])
                      print()
                     else:
                             print('You are in the corn field. There man with the severed arm is lying here on the ground, dead.')
                             print()

                    elif start == 'la':
                      if deadinfield == 0:
                             
                       print(greet['la'])
                       print()
                      else:
                             print('You are in the corn field. There man with the severed arm is lying here on the ground, dead.')
                             print()
                      
                    elif start == 'south':
                      print(greet['south'])
                      print()

                    elif start == 'go south':
                      print(greet['south'])
                      print()

                    elif start == 'west':
                      print(greet['west'])
                      print()

                    elif start == 'go west':
                      print(greet['west'])
                      print()

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    elif start == 'field':
                      print(greet['field'])
                      print()

                    elif start == 'look at field':
                      print(greet['field'])
                      print()

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
















##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################




                
# 1: place = ['yard']-------------------------------------------------------------------------------------------------------------------------------------------

        elif place == ['yard']:
                
         
         mapb = 1
         
         greet = { 'ihy' : 'Ow, my heart!',
                     'ily1' : 'Whoa now! That\'s a titch strong',
                     'la1'  : 'You come out of the field and see a small house with a barn next to it. There is a heavy smell of amonia and feces. There is no one around but you can hear what\nseems like howling in the distance.',      
                     'la'   : 'You see a small house with a barn next to it. There is a heavy smell of ammonia in the air. There is no one around but you can hear what seems like howling in\nthe distance. From here you can go to the barn, the house, or go to the east of the house.',      
                     'hey' : 'What\'s goin on?',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down like a loon. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?',
                     'house'  : 'You are in front of the house. All of the windows are boarded up. You try the\ndoor. It\'s locked but seems like it could be kicked in. You see next to the doora flashlight.',
                     'kd'     : 'You aim, step back, and BAM! The door comes off the hinges and slams on the floor in front\nof you.',
                     'ydht'   : 'You don\'t have that yet',
                     'light'  : 'You don\'t have a  flashlight.',
                     'takenf' : 'You don\'t see a flashlight here.'
                     


                         }
         yard = 1
         while yard == 1:
                 
        

    
    
               
            
                
              
                
                
                
                print('Yard')
                start = input('You: ').lower()
                print()
                
                if start == 'quit':
                  print('Bye Bye')
                  
                  place = ['20']
                  yard = 0
                  running = 0

                elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()                
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                elif start == 'go to the east of the house':
                        print('You head to the east of the house.')
                        print()
                        place = ['yardr']
                        yard = 0


                elif start == 'go east':
                        print('You head to the east of the house.')
                        print()
                        place = ['yardr']
                        yard = 0


                elif start == 'east':
                        print('You head to the east of the house.')
                        print()
                        place = ['yardr']
                        yard = 0



                elif start == 'go to the right of the house':
                        print('You head to the east of the house.')
                        print()
                        place = ['yardr']
                        yard = 0

                elif start == 'go right':
                        print('You head to the east of the house.')
                        print()
                        place = ['yardr']
                        yard = 0

                elif start == 'field':
                        print('You head back to the field.')
                        print()
                        place = ['field']
                        yard = 0

                elif start == 'go to field':
                        print('You head back to the field.')
                        print()
                        place = ['field']
                        yard = 0

                elif start == 'go back to field':
                        print('You head back to the field.')
                        print()
                        place = ['field']
                        yard = 0

                elif start == 'shed':
                        if mapc == 1:
                                print('You head back to the old shed.')
                                print()
                                yard = 0
                                place = ['shed']

                        else:
                                print('You can\'t see a shed from here.')
                                print()
                        
                        

                elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                  
                  
                  

                elif start == 'south':
                    print('You go back to the field you started in.')
                    print()
                    
                    place = ['field']
                    yard = 0
                    
                    
                   
                    
                
                    

                elif start == 'go south':
                    print('You go back to the field you started in.')
                    print()

                    place = ['field']
                    yard = 0

                elif start == 'go back':
                    print('You go back to the field you started in.')
                    print()

                    place = ['field']
                    yard = 0

                elif start == 'barn':
                        if 'flashlight' not in items:
                                
                                print('You come up to the worn-down barn. You open the door but it is too dark to see inside. You could go further if you had a flashlight.')
                                print()
                                place = ['barn']
                                yard = 0

                        else:
                                print('You come up to the word-down barn. You now have a flashlight so you can go in if you like.')
                                print()
                                place = ['barn']
                                yard = 0
                                

                elif start == 'go to barn':
                        if 'flashlight' not in items:
                        
                                print('You come up to the worn-down barn. You open the door but it is too dark to see inside. You could go further if you had a flashlight.')
                                print()
                                place = ['barn']
                                yard = 0

                        else:
                                print('You come up to the word-down barn. You now have a flashlight so you can go in if you like.')
                                print()
                                place = ['barn']
                                yard = 0

                elif start == 'house':
                        print('You come up to the porch of the house.')
                        print()
                        place = ['house']
                        yard = 0

                elif start == 'go to house':
                        print('You come up to the porch of the house.')
                        print()
                        place = ['house']
                        yard = 0

                    
                    
                    
                   
                    
                  

                    
                  

                elif start == 'i hate you':
                  print(greet['ihy'])
                  print()

                elif start == 'check items':
                  if items == []:
                     print('You don\'t have any at the moment')
                     print()
                  else:
                     print(items)
                     print()

                elif start == 'items':
                  if items == []:
                     print('You don\'t have any at the moment')
                     print()
                  else:
                     print(items)
                     print()

                

                elif start == 'eat corn':
                  if 'corn' in items:
                     print('You take the ear and gobble it down. Delicious')
                     items.remove('corn')
                     print()
                  else:
                     print('You don\'t have any corn in your items')
                     print()

                elif start == 'throw corn':
                  if 'corn' in items:
                     where = input('Where do you want to throw the corn? ').lower()
                     
                     if where == 'me':
                        items.remove('corn')
                        print('OW! Why would you do that to yourself?!')
                        print()
                        
                     elif where == 'there':
                        print('You throw the corn over there.')
                        print()
                        items.remove('corn')
                        
                     elif where == 'bird':
                        print('You can\'t see any bird around.')
                        print()

                     elif where == 'you':
                        print('Yeah, you wish you could hit this!')
                        print()

                     else:
                        print('You can\'t do that.')
                        print()

                  else:
                     print('You don\'t have any corn to throw')
                     print()
                 

                  

                elif start == 'fag':
                  print(greet['fag'])
                  print()

                elif start == 'faggot':
                  print(greet['fag'])
                  print()

                elif start == 'you suck':
                  print(greet['ys'])
                  print()

                elif start == 'whatever':
                  print(greet['mmm'])
                  print()

                elif start == 'how are you':
                  print(greet['pg'])
                  print()

                elif start == 'fagget':
                  print(greet['spell'])
                  print()

                elif start == 'fagg':
                  print(greet['spell'])
                  print()

                elif start == 'jump':
                  print(greet['jump'])
                  print()

                elif start == 'dance':
                  print(greet['dance'])
                  print()

                elif start == 'sing':
                  print(greet['sing'])
                  print()

                elif start == 'fuck you':
                  print(greet['fu'])
                  print()

                elif start == 'smile':
                  print(greet['smile'])
                  print()

                elif start == 'grin':
                  print(greet['grin'])
                  print()

                elif start == 'bitch':
                  print(greet['ho'])
                  print()

                elif start == 'i don\'t like you':
                  print(greet['idly'])
                  print()

                elif start == 'i love you':
                  print(greet['ily'])
                  print()

                elif start == 'hey':
                  print(greet['hey'])
                  print()

                elif start == 'hi':
                  print(greet['heyt'])
                  print()

                elif start == 'hello':
                  print(greet['hello'])
                  print()

                elif start == 'dude':
                  print(greet['dude'])
                  print()

                elif start == 'sweet':
                  print(greet['sweet'])
                  print()   

                elif start == 'you':
                  print(greet['crank'])
                  print()   
                  
                elif start == 'look around':
                  print(greet['la'])
                  print()

                elif start == 'la':
                  print(greet['la'])
                  print()
                  
                elif start == 'south':
                  print(greet['south'])
                  print()

                elif start == 'go south':
                  print(greet['south'])
                  print()

                elif start == 'west':
                  print(greet['west'])
                  print()

                elif start == 'go west':
                  print(greet['west'])
                  print()

                

                elif start == 'damn':
                  print(greet['cuss'])
                  print()

                elif start == 'you bastard':
                  print(greet['yb'])
                  print()

                elif start == 'fuck':
                  print(greet['cuss'])
                  print()

                elif start == 'shit':
                  print(greet['cuss'])
                  print()

                

                elif start == 'what\'s up':
                  print(greet['whatup'])
                  print()

                else:
                    print('I don\'t know the word(s): ' + start )
                    print()



















##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# 2: place = ['shed']-------------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['shed']:

              

              mapc = 1
                
        
    
      
              greet = { 'ihy' : 'Well I\'m not too fond of you either.',
             'ily' : 'Whoa now! That\'s a little strong.',
             'la'  : 'You are in front of an old shed. There is a trail leading north and the shed door to the east. There is also some object being illuminated by the moon on the ground next to the shed. What is that!',
             'east': 'You walk out from the field and come upon an old shed. There is a trail leading north. There is also a light pointing down from the top and is illuminating something. What is that!',
             'hey'  : 'What\'s up?',
             'south': 'You can\'t go south.',
             'west' : 'You can\'t go west.',
             'music': 'This is Mozart\'s Requiem Mass in D Minor.',
             'cuss' : 'Ha Ha! Getting frustrated?',
             'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
             'dude' : 'Sweet!',
             'whatup' : 'Nothing much, how about yourself?',
             'heyt'   : 'Hey there.',
             'hello'  : 'Hello.',
             'crank'  : 'crank that soulja boy!',
             'sweet'  : 'Dude!',
             'fu'     : 'Fuck you too!',
             'ho'     : 'Ho.',
             'idly'   : 'Whateva.',
             'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
             'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
             'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
             'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
             'yb'     : 'tee hee',
             'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
             'fag'    : 'See a mirror or something?',
             'spell'  : 'Ha! Way to misspell while trying to insult me!',
             'mmm'    : 'Mm Hmm',
             'pg'     : 'Pretty good. How \'bout yourself?',
             'ys'     : 'Yo Momma!',
             'take'   : 'What do you want to take?'

                 }
              east = 1
      
              while east == 1:

                                 if arm == 1:
                                         greet['la'] = 'You are in front of the old shed. There is a trail leading north and one leading south back to the field.'
                                 else:
                                         greet['la'] = 'You are in front of an old shed. There is a trail leading north and one leading south back to the field. There is also something being illuminated by the moon next to the shed. What is that?!'

                                 print('Front of Shed')        
                                 start = input('You: ').lower()
                                 print()

                                 if start == 'quit':
                                    print('Bye Bye')
                              
                                    running = 0
                                    place = ['20']
                                    east = 0

                                 elif start == 'read letter':
                                    if 'letter' in items:
                                            print(letter)
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                                 elif start == 'i love katie':
                                            print('The very mostest babe!')
                                            print()

                                 elif start == 'i love jp':
                                            print('Who doesn\'t?')
                                            print()

                                 elif start == 'examine':
                                            print('What do you want to examine?')
                                            print()
                                            ex = input('...').lower()
                                            if ex == 'corn':
                                                    if 'corn' in items:
                                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                                            print()

                                                    else:
                                                            print('You don\'t have any corn to examine.')
                                                            print()
                                            elif ex == 'truck keys':
                                                    if 'truck keys' in items:
                                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                                            print()

                                                    else:
                                                            print('You don\'t have any keys to examine.')
                                                            print()
                                            elif ex == 'keys':
                                                    if 'truck keys' in items:
                                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                                            print()

                                                    else:
                                                            print('You don\'t have any keys to examine.')
                                                            print()
                                            elif ex == 'severed arm':
                                                    if 'severed arm' in items:
                                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                                            print()

                                                    else:
                                                            print('You do not have one of those.')
                                                            print()

                                            elif ex == 'letter':
                                                    if 'letter' in items:
                                            
                                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                                            print()

                                                    else:
                                                            print('You don\'t have a letter.')
                                                            print()

                                            elif ex == 'boat plug':
                                                    if 'boat plug' in items:
                                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                                            print()

                                                    else:
                                                            print('You don\'t have a boat plug.')
                                                            print()

                                            elif ex == 'plug':
                                                    if 'boat plug' in items:
                                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                                            print()

                                                    else:
                                                            print('You don\'t have a boat plug.')
                                                            print()
                                                    
                                            elif ex == 'note':
                                                    if 'barn note' in items:
                                                            
                                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                                            print()

                                                    else:
                                                            print('You don\'t have a note to examine.')
                                                            print()

                                            elif ex == 'barn note':
                                                    if 'barn note' in items:
                                                            
                                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                                            print()

                                                    else:
                                                            print('You don\'t have a note to examine.')
                                                            print()

                                            elif ex == 'arm':
                                                    if 'severed arm' in items:
                                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                                            print()

                                                    else:
                                                            print('You do not have one of those.')
                                                            print()

                                            elif ex == 'flashlight':
                                                    if 'flashlight' in items:
                                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                                            print()

                                                    else:
                                                            print('You don\'t have a flashlight.')
                                                            print()

                                            elif ex == 'machete':
                                                    if 'machete' in items:
                                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                                            print()

                                                    else:
                                                            print('You don\'t have a machete.')
                                                            print()
                                                            

                                            else:
                                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                                    print()

                                 elif start == 'house':
                                         if mapb == 1:
                                                 print('You head back in front of the house.')
                                                 print()
                                                 place = ['house']
                                                 east = 0

                                         else:
                                                 print('You can\'t see a house from here.')
                                                 print()

                                 elif start == 'field':
                                         
                                                 print('You head back to the field.')
                                                 print()
                                                 place = ['field']
                                                 east = 0

                                 elif start == 'barn':
                                         if mapb == 1:
                                                 print('You head back in front of the barn.')
                                                 print()
                                                 place = ['barn']
                                                 east = 0

                                         else:
                                                 print('You can\'t see a barn from here.')
                                                 print()

                                         

                                 elif start == 'read barn note':
                                    if 'barn note' in items:
                                            print(barnnote)
                                            print()
                                    else:
                                            print('You don\'t have that yet.')
                                            print()

                                 elif start == 'read note':
                                    if 'barn note' in items:
                                            print(barnnote)
                                            print()
                                    else:
                                            print('You don\'t have that yet.')
                                            print()

                                 elif start == 'what is that':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1
                                         else:
                                                 print('It is a severed arm.')
                                                 print()
                                         

                                 elif start == 'look at object':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1
                                         else:
                                                 print('It is a severed arm.')
                                                 print()

                                 elif start == 'look at it':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1
                                         else:
                                                 print('It is a severed arm.')
                                                 print()

                                 elif start == 'look':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1
                                         else:
                                                 print('It is a severed arm.')
                                                 print()

                                 elif start == 'examine object':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1

                                         elif arm == 1:
                                                 print('You look closer and see that the arm appears to have been bitten down to the bone and then was ripped from the body. You get chills all over your body and you become very sick. You vomit on the ground nearby.')
                                                 print()
                                                 exarm = 1

                                                 
                                         else:
                                                 print('It is a severed arm.')
                                                 print()

                                 
                                                 
                                 elif start == 'see what it is':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1
                                         else:
                                                 print('It is a severed arm.')
                                                 print()


                                 elif start == 'what is it':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1
                                         else:
                                                 print('It is a severed arm.')
                                                 print()
                                         
                                 elif start == 'what is the object':
                                         if arm == 0:
                                                 
                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                 print()
                                                 arm = 1
                                         else:
                                                 print('It is a severed arm.')
                                                 print()

                                 elif start == 'take arm':
                                         if arm == 1:
                                                 
                                                 print('Are you sure you want to take the severed arm?')
                                                 noyes = input().lower()
                                                 if noyes == 'yes':
                                                         print('OK then. You pick up the bloody severed arm and stuff it in your back pocket. You can feel the cold, wet blood dripping down the back of your pants.')
                                                         print()
                                                         items.append('severed arm')

                                                 elif noyes == 'no':
                                                         print('That\'s what  I thought.')
                                                         print()

                                                 else:
                                                         print('If you\'re not going to give me a "yes" or a "no", I can\'t help you.')
                                                         print()

                                         else:
                                                 print('What are you talking about?')
                                                 print()

                                 elif start == 'go inside':
                                         if 'flashlight' in items:
                                                 if arm == 0:
                                                         if 'severed arm' not in items:
                                                                 

                                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                                 arm = 1
                                                                 print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                 print()
                                                 
                                                                 place = ['inshed']
                                                                 east = 0
                                                         
                                                         else:
                                                                 print('You head inside the old shed.')
                                                                 print()

                                                 else:
                                                        if 'severed arm' not in items:
                                                                
                                                                print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0

                                                        else:
                                                                print('You head inside the shed.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0
                                                        
                                         else:
                                                 if arm == 0:
                                                         print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                         print()
                                                         arm = 1
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1

                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()
                                                 else:
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1
                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()




                                                         

                                
                                 elif start == 'go in':
                                          if 'flashlight' in items:
                                                 if arm == 0:
                                                         if 'severed arm' not in items:
                                                                 

                                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                                 arm = 1
                                                                 print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                 print()
                                                 
                                                                 place = ['inshed']
                                                                 east = 0
                                                         
                                                         else:
                                                                 print('You head inside the old shed.')
                                                                 print()

                                                 else:
                                                        if 'severed arm' not in items:
                                                                
                                                                print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0

                                                        else:
                                                                print('You head inside the shed.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0
                                                        
                                          else:
                                                 if arm == 0:
                                                         print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                         print()
                                                         arm = 1
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1

                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()
                                                 else:
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1
                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()
                                         

                                 elif start == 'map':

                                            if mapa == 1:
                                                    if mapb == 1:
                                                            if mapc == 1:
                                                                    if mapofpond == 1:
                                                                            if mapfront == 1:
                                                                                    print(MAPOFPONDTRUCK)
                                                                                    print()

                                                                            else:
                                                                                    print(MAPOFPONDNOTRUCK)
                                                                                    print()

                                                                    elif mapfront == 1:
                                                                            if mapofpond == 1:
                                                                                    print(MAPOFPONDTRUCK)
                                                                                    print()
                                                                            else:
                                                                                    print(MAPFRONTOFHOUSE)
                                                                                    print()
                                                                                    

                                                                    else:
                                                                            
                                                                        
                                                                            print(MAPD)
                                                                            print()
                                                            elif mapfront == 1:
                                                                    if mapc == 1:
                                                                            print(MAPFRONTOFHOUSE)
                                                                            print()
                                                                            
                                                                    else:
                                                                            
                                                                            print(MAPFRONTOFHOUSENOEAST)
                                                                            print()

                                                            


                                                            else:
                                                                    
                                                                    print(MAPB)
                                                                    print()
                                                    elif mapc == 1:
                                                            if mapb == 1:
                                                                    if mapofpond == 1:
                                                                            if mapfront == 1:
                                                                                    print(MAPOFPONDTRUCK)
                                                                                    print()

                                                                            else:
                                                                                    print(MAPOFPONDNOTRUCK)
                                                                                    print()

                                                                    elif mapfront == 1:
                                                                            if mapofpond == 1:
                                                                                    print(MAPOFPONDTRUCK)
                                                                                    print()
                                                                            else:
                                                                                    print(MAPFRONTOFHOUSE)
                                                                                    print()
                                                                                    

                                                                    else:
                                                                            
                                                                        
                                                                            print(MAPD)
                                                                            print()
                        

                                                            elif mapfront == 1:
                                                                    if mapofpond == 1:
                                                                            print(MAPOFPONDTRUCK)
                                                                            print()

                                                                    else:
                                                                            print(MAPFRONTOFHOUSENOBARN)


                                                            elif rightofhouse == 1:
                                                                    print(YRMAP1)
                                                                    print()
                                                            else:
                                                                    
                                                                    print(MAPC)
                                                                    print()

                                                 

                                                    
                                                    else:
                                                            print(MAPA)
                                                            print()

                                 elif start == 'north':
                                         print('You head up the trail leading north.')
                                         print()
                                         place = ['yardr']
                                         east = 0

                                 elif start == 'go north':
                                         print('You head up the trail leading north.')
                                         print()
                                         place = ['yardr']
                                         east = 0

                                 elif start == 'i hate you':
                                    print(greet['ihy'])
                                    print()

                                 elif start == 'check items':
                                    if items == []:
                                       print('You don\'t have any at the moment')
                                       print()
                                    else:
                                       print(items)
                                       print()

                                 elif start == 'items':
                                    if items == []:
                                       print('You don\'t have any at the moment')
                                       print()
                                    else:
                                       print(items)
                                       print()

                                 
                                 elif start == 'throw corn':
                                    if 'corn' in items:
                                       where = input('Where do you want to throw the corn? ').lower()
                                       
                                       if where == 'me':
                                          items.remove('corn')
                                          print('OW! Why would you do that to yourself?!')
                                          print()
                                          
                                       elif where == 'there':
                                          print('You throw the corn over there.')
                                          print()
                                          items.remove('corn')
                                          
                                       elif where == 'bird':
                                          print('You can\'t see any bird around.')
                                          print()

                                       elif where == 'you':
                                          print('Yeah, you wish you could hit this!')
                                          print()

                                       else:
                                          print('You can\'t do that.')
                                          print()

                                    else:
                                       print('You don\'t have any corn to throw')
                                       print()
                                   

                                    

                                 elif start == 'fag':
                                    print(greet['fag'])
                                    print()

                                 elif start == 'faggot':
                                    print(greet['fag'])
                                    print()

                                 elif start == 'you suck':
                                    print(greet['ys'])
                                    print()

                                 elif start == 'whatever':
                                    print(greet['mmm'])
                                    print()

                                 elif start == 'how are you':
                                    print(greet['pg'])
                                    print()

                                 elif start == 'fagget':
                                    print(greet['spell'])
                                    print()

                                 elif start == 'fagg':
                                    print(greet['spell'])
                                    print()

                                 elif start == 'jump':
                                    print(greet['jump'])
                                    print()

                                 elif start == 'dance':
                                    print(greet['dance'])
                                    print()

                                 elif start == 'sing':
                                    print(greet['sing'])
                                    print()

                                 elif start == 'fuck you':
                                    print(greet['fu'])
                                    print()

                                 elif start == 'smile':
                                    print(greet['smile'])
                                    print()

                                 elif start == 'grin':
                                    print(greet['grin'])
                                    print()

                                 elif start == 'bitch':
                                    print(greet['ho'])
                                    print()

                                 elif start == 'i don\'t like you':
                                    print(greet['idly'])
                                    print()

                                 elif start == 'i love you':
                                    print(greet['ily'])
                                    print()

                                 elif start == 'hey':
                                    print(greet['hey'])
                                    print()

                                 elif start == 'hi':
                                    print(greet['heyt'])
                                    print()

                                 elif start == 'hello':
                                    print(greet['hello'])
                                    print()

                                 elif start == 'dude':
                                    print(greet['dude'])
                                    print()

                                 elif start == 'sweet':
                                    print(greet['sweet'])
                                    print()   

                                 elif start == 'you':
                                    print(greet['crank'])
                                    print()   
                                    
                                 elif start == 'look around':
                                         if arm == 0:
                                                 
                                            print(greet['la'])
                                            print()

                                         else:
                                                 if 'severed arm' in items:
                                                         print('You are in front of an old shed. There is a trail leading north and the shed door to the east.')
                                                         print()

                                                 else:
                                                         print('You are in front of an old shed. There is a severed arm lying on the ground. There is a trail leading north and the shed door to the east.')
                                                         print()
                                                               

                                                 

                                 elif start == 'la':
                                    if arm == 0:
                                                 
                                            print(greet['la'])
                                            print()

                                    else:
                                                 if 'severed arm' in items:
                                                         print('You are in front of an old shed. There is a trail leading north and the shed door to the east.')
                                                         print()

                                                 else:
                                                         print('You are in front of an old shed. There is a severed arm lying on the ground. There is a trail leading north and the shed door to the east.')
                                                         print()
                                    
                                 elif start == 'south':
                                    print('You turn around and go back to the field where you woke up')
                                    print()
                                    place = ['field']
                                    east = 0

                                 elif start == 'go south':
                                    print('You turn around and go back to the field where you woke up')
                                    print()
                                    place = ['field']
                                    east = 0

                                 elif start == 'go back':
                                    print('You turn around and go back to the field where you woke up')
                                    print()
                                    place = ['field']
                                    east = 0

                                 elif start == 'west':
                                    print('You can\'t go west')
                                    print()

                                 elif start == 'go west':
                                    print('You can\'t go west')
                                    print()


                                 elif start == 'go east':
                                    if 'flashlight' in items:
                                                 if arm == 0:
                                                         if 'severed arm' not in items:
                                                                 

                                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                                 arm = 1
                                                                 print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                 print()
                                                 
                                                                 place = ['inshed']
                                                                 east = 0
                                                         
                                                         else:
                                                                 print('You head inside the old shed.')
                                                                 print()

                                                 else:
                                                        if 'severed arm' not in items:
                                                                
                                                                print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0

                                                        else:
                                                                print('You head inside the shed.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0
                                                        
                                    else:
                                                 if arm == 0:
                                                         print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                         print()
                                                         arm = 1
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1

                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()
                                                 else:
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1
                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()

                                 elif start == 'east':
                                    if 'flashlight' in items:
                                                 if arm == 0:
                                                         if 'severed arm' not in items:
                                                                 

                                                                 print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                                 arm = 1
                                                                 print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                 print()
                                                 
                                                                 place = ['inshed']
                                                                 east = 0
                                                         
                                                         else:
                                                                 print('You head inside the old shed.')
                                                                 print()

                                                 else:
                                                        if 'severed arm' not in items:
                                                                
                                                                print('You walk past the severed arm and reluctantly head inside the old shed, following the trail of blood.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0

                                                        else:
                                                                print('You head inside the shed.')
                                                                print()
                                                                place = ['inshed']
                                                                east = 0
                                                        
                                    else:
                                                 if arm == 0:
                                                         print('You walk up to the object and see that it\'s a severed arm! What in the world is going on?! You also see a trail of blood leading inside the shed.')
                                                         print()
                                                         arm = 1
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1

                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()
                                                 else:
                                                         if eastopen == 0:
                                                                 
                                                                 print('You open the door but it is pitch-black dark inside and you cannot find a light switch. You can\'t go forward without a light source of some kind.')
                                                                 print()
                                                                 eastopen = 1
                                                         else:
                                                                 print('It is pitch-black dark inside and you cannot find a light switch. You cannot go further without a light.')
                                                                 print()

                                 

                                 elif start == 'damn':
                                    print(greet['cuss'])
                                    print()

                                 elif start == 'you bastard':
                                    print(greet['yb'])
                                    print()

                                 elif start == 'fuck':
                                    print(greet['cuss'])
                                    print()

                                 elif start == 'shit':
                                    print(greet['cuss'])
                                    print()

                                 

                                 elif start == 'what\'s up':
                                    print(greet['whatup'])
                                    print()

                                
                                    




                                    

                                 

                                 else:
                                    print('I don\'t know the word(s): ' + start)




























##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# place = ['yardr']----------------------------------------------------------------------------------------------------------------------------------------------

        elif place == ['yardr']:

                rightofhouse = 1
                
                
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are at the right side of the house. You can\'t see much other than the yard to the south, the front of the house to the north, and a trail to the east.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }
                yardr = 1
                while yardr == 1:


                    print('Right of House')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      yardr = 0
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                    elif start == 'go to barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    yardr = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                    elif start == 'barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    yardr = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                      
                      
                    elif start == 'go to shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    yardr = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()

                    elif start == 'shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    yardr = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()
                     
                      

                    elif start == 'go to house':
                            
                                    print('You head to the house.')
                                    print()
                                    yardr = 0
                                    place = ['house']

                            
                                   
                    elif start == 'house':
                            
                                    print('You head to the house.')
                                    print()
                                    yardr = 0
                                    place = ['house']

                            




                    elif start == 'go to the house':
                            
                                    print('You head to the house.')
                                    print()
                                    yardr = 0
                                    place = ['house']

                           

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
                            

                                    
                      
                    elif start == 'north':
                            print('You head to the front of the house.')
                            print()
                            place = ['fronthouse']
                            yardr = 0

                    elif start == 'go north':
                            print('You head to the front of the house.')
                            print()
                            place = ['fronthouse']
                            yardr = 0
                            
                     

                                   
                        
                        
                     
                        
                
                        
                    
                        
                        

                                   
                        
                    
                    elif start == 'east':
                            print('You head down the trail to the east.')
                            print()
                            yardr = 0
                            place = ['shed']
                            

                    elif start == 'go east':
                            print('You head down the trail to the east.')
                            print()
                            yardr = 0
                            place = ['shed']
                       
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                   

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('You really don\'t feel like it but oh well. You jump up and down and now feel quite foolish and out of breath.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                      print(greet['la'])
                      print()

                    elif start == 'la':
                      print(greet['la'])
                      print()
                      
                    elif start == 'south':
                      print('You head to the yard.')
                      print()
                      yardr = 0
                      place = ['yard']

                    elif start == 'go south':
                      print('You head to the yard.')
                      print()
                      yardr = 0
                      place = ['yard']

                    elif start == 'west':
                      print(greet['west'])
                      print()

                    elif start == 'go west':
                      print(greet['west'])
                      print()

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
                




























##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################




                                       
# 3: place = ['barn']-------------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['barn']:
                
                
                greet = { 'ihy' : 'Well I\'m not too fond of you either.',
             'ily' : 'Whoa now! That\'s a little strong.',
             'la'  : 'You are in front of the worn-down barn. You can\'t go inside without a light of some kind.',
             'north': 'You walk out from the field to see a small house with a red worn barn to the left of it. There is an overbearing smell of ammonia in the air. In the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
             'hey'  : 'What\'s up?',
             'south': 'You can\'t go south.',
             'west' : 'You can\'t go west.',
             'music': 'This is Mozart\'s Requiem Mass in D Minor.',
             'cuss' : 'Ha Ha! Getting frustrated?',
             'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
             'dude' : 'Sweet!',
             'whatup' : 'Nothing much, how about yourself?',
             'heyt'   : 'Hey there.',
             'hello'  : 'Hello.',
             'crank'  : 'crank that soulja boy!',
             'sweet'  : 'Dude!',
             'fu'     : 'Fuck you too!',
             'ho'     : 'Ho.',
             'idly'   : 'Whateva.',
             'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
             'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
             'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
             'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
             'yb'     : 'tee hee',
             'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
             'fag'    : 'See a mirror or something?',
             'spell'  : 'Ha! Way to misspell while trying to insult me!',
             'mmm'    : 'Mm Hmm',
             'pg'     : 'Pretty good. How \'bout yourself?',
             'ys'     : 'Yo Momma!',
             'take'   : 'What do you want to take?'

                 }

                barn = 1
                while barn == 1:

                           print('Front of Barn')
                           start = input('You: ').lower()
                           print()
                           if start == 'quit':
                              print('Bye Bye')
                              barn = 0
                              running = 0

                           elif start == 'read letter':
                                    if 'letter' in items:
                                            print(letter)
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()


                           elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                           elif start == 'i love jp':
                                    print('Who doesn\'t?')
                                    print()

                           elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                           elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                           elif start == 'go in':
                                   if 'flashlight' in items:
                                           print('You head inside the barn.')
                                           print()
                                           place = ['inbarn']
                                           barn = 0

                                   else:
                                           print('You can\'t go in without a flashlight.')
                                           print()

                           elif start == 'go inside':
                                   if 'flashlight' in items:
                                           print('You head inside the barn.')
                                           print()
                                           place = ['inbarn']
                                           barn = 0

                                   else:
                                           print('You can\'t go in without a flashlight.')
                                           print()


                           

                           elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()

                           elif start == 'i hate you':
                              print(greet['ihy'])
                              print()

                           elif start == 'check items':
                              if items == []:
                                 print('You don\'t have any at the moment')
                                 print()
                              else:
                                 print(items)
                                 print()

                           elif start == 'items':
                              if items == []:
                                 print('You don\'t have any at the moment')
                                 print()
                              else:
                                 print(items)
                                 print()

                           

                           elif start == 'eat corn':
                              if 'corn' in items:
                                 print('You take the ear and gobble it down. Delicious')
                                 items.remove('corn')
                                 print()
                              else:
                                 print('You don\'t have any corn in your items')
                                 print()

                           elif start == 'throw corn':
                              if 'corn' in items:
                                 where = input('Where do you want to throw the corn? ').lower()
                                 
                                 if where == 'me':
                                    items.remove('corn')
                                    print('OW! Why would you do that to yourself?!')
                                    print()
                                    
                                 elif where == 'there':
                                    print('You throw the corn over there.')
                                    print()
                                    items.remove('corn')
                                    
                                 elif where == 'bird':
                                    print('You can\'t see any bird around.')
                                    print()

                                 elif where == 'you':
                                    print('Yeah, you wish you could hit this!')
                                    print()

                                 else:
                                    print('You can\'t do that.')
                                    print()

                              else:
                                 print('You don\'t have any corn to throw')
                                 print()
                             

                              

                           elif start == 'fag':
                              print(greet['fag'])
                              print()

                           elif start == 'faggot':
                              print(greet['fag'])
                              print()

                           elif start == 'you suck':
                              print(greet['ys'])
                              print()

                           elif start == 'whatever':
                              print(greet['mmm'])
                              print()

                           elif start == 'how are you':
                              print(greet['pg'])
                              print()

                           elif start == 'fagget':
                              print(greet['spell'])
                              print()

                           elif start == 'fagg':
                              print(greet['spell'])
                              print()

                           elif start == 'jump':
                              print(greet['You jump up and down and begin to breath heavily.'])
                              print()

                           elif start == 'dance':
                              print(greet['dance'])
                              print()

                           elif start == 'sing':
                              print(greet['sing'])
                              print()

                           elif start == 'fuck you':
                              print(greet['fu'])
                              print()

                           elif start == 'smile':
                              print(greet['smile'])
                              print()

                           elif start == 'grin':
                              print(greet['grin'])
                              print()

                           elif start == 'bitch':
                              print(greet['ho'])
                              print()

                           elif start == 'i don\'t like you':
                              print(greet['idly'])
                              print()

                           elif start == 'i love you':
                              print(greet['ily'])
                              print()

                           elif start == 'hey':
                              print(greet['hey'])
                              print()

                           elif start == 'hi':
                              print(greet['heyt'])
                              print()

                           elif start == 'hello':
                              print(greet['hello'])
                              print()

                           elif start == 'dude':
                              print(greet['dude'])
                              print()

                           elif start == 'sweet':
                              print(greet['sweet'])
                              print()   

                           elif start == 'you':
                              print(greet['crank'])
                              print()   
                              
                           elif start == 'look around':
                              print(greet['la'])
                              print()

                           elif start == 'la':
                              print(greet['la'])
                              print()
                              
                           elif start == 'south':
                              print('You head back to the yard.')
                              print()
                              place = ['yard']
                              barn = 0

                           elif start == 'go south':
                              print('You head back to the yard.')
                              print()
                              place = ['yard']
                              barn = 0

                           elif start == 'go back':
                              print('You head back to the yard.')
                              print()
                              place = ['yard']
                              barn = 0

                           elif start == 'west':
                              print(greet['west'])
                              print()

                           elif start == 'go west':
                              print(greet['west'])
                              print()

                           

                           elif start == 'damn':
                              print(greet['cuss'])
                              print()

                           elif start == 'you bastard':
                              print(greet['yb'])
                              print()

                           elif start == 'fuck':
                              print(greet['cuss'])
                              print()

                           elif start == 'shit':
                              print(greet['cuss'])
                              print()

                           

                           

                           elif start == 'what\'s up':
                              print(greet['whatup'])
                              print()

                           else:
                                print('I don\'t know the word(s): ' + start)
                                print()
























##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# 4: place = ['house']--------------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['house']:
                
                greet = { 'ihy' : 'Well I\'m not too fond of you either.',
             'ily' : 'Whoa now! That\'s a little strong.',
             'la'  : 'You are on the porch of the house. All of the windows are boarded up and the door is locked, but it seems it can be kicked in. There is a flashlight on the porch.',
             'north': 'You walk out from the field to see a small house with a red worn barn to the left of it. There is an overbearing smell of ammonia in the air. In the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
             'hey'  : 'What\'s up?',
             'south': 'You can\'t go south.',
             'west' : 'You can\'t go west.',
             'music': 'This is Mozart\'s Requiem Mass in D Minor.',
             'cuss' : 'Ha Ha! Getting frustrated?',
             'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
             'dude' : 'Sweet!',
             'whatup' : 'Nothing much, how about yourself?',
             'heyt'   : 'Hey there.',
             'hello'  : 'Hello.',
             'crank'  : 'crank that soulja boy!',
             'sweet'  : 'Dude!',
             'fu'     : 'Fuck you too!',
             'ho'     : 'Ho.',
             'idly'   : 'Whateva.',
             'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
             'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
             'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
             'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
             'yb'     : 'tee hee',
             'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
             'fag'    : 'See a mirror or something?',
             'spell'  : 'Ha! Way to misspell while trying to insult me!',
             'mmm'    : 'Mm Hmm',
             'pg'     : 'Pretty good. How \'bout yourself?',
             'ys'     : 'Yo Momma!',
             'take'   : 'What do you want to take?'

                 }
                

                                

                house = 1
                while house == 1:

                           if 'flashlight' in items:
                                if door == 1:
                                
                                        greet['la'] = 'You are on the porch of the house. All of the windows are boarded up but the door has been kicked in.'

                                else:
                                        greet['la'] = 'You are on the porch of the house. All of the windows are boarded up but the door looks like it could be kicked in.'

                           else:
                                   if door == 1:
                                
                                        greet['la'] = 'You are on the porch of the house. All of the windows are boarded up but the door has been kicked in. There is a flashlight here.'

                                   else:
                                        greet['la'] = 'You are on the porch of the house. All of the windows are boarded up and the door is locked, but it seems it can be kicked in. There is a flashlight on the porch.'

                           print('Porch of House')
                           start = input('You: ').lower()
                           print()
                                   
                           if start == 'quit':
                              print('Bye Bye')
                              house = 0
                              running = 0

                           elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                           elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                           elif start == 'i love jp':
                                    print('Who doesn\'t?')
                                    print()

                           elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                                            
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                           elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                           elif start == 'go in':
                                   if door == 0:
                                           print('You can\'t go inside unless you find a way in.')
                                           print()
                                   elif door == 1:
                                           if 'flashlight' not in items:
                                                   print('You can\'t go in without a flashlight.')
                                                   print()
                                           else:
                                                    print('You head inside the house and you come into a living room.')
                                                    print()
                                                    place = ['livingroom']
                                                    house = 0

                           elif start == 'go inside':
                                   if door == 0:
                                           print('You can\'t go inside unless you find a way in.')
                                           print()
                                   elif door == 1:
                                           if 'flashlight' not in items:
                                                   print('You can\'t go in without a flashlight.')
                                                   print()
                                           else:
                                                    print('You head inside the house and you find yourself in a living room.')
                                                    print()
                                                    place = ['livingroom']
                                                    house = 0

                           elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                           

                           elif start == 'i hate you':
                              print(greet['ihy'])
                              print()

                           elif start == 'go back':
                                   print('You head back to the yard.')
                                   print()
                                   place = ['yard']
                                   house = 0

                           elif start == 'go south':
                                   print('You head back to the yard.')
                                   print()
                                   place = ['yard']
                                   house = 0

                           elif start == 'south':
                                   print('You head back to the yard.')
                                   print()
                                   place = ['yard']
                                   house = 0

                           elif start == 'take flashlight':
                                   if 'flashlight' in items:
                                           print('You already have the flashlight.')
                                           print()
                                   else:
                                           print('You take the flashlight.')
                                           print()
                                           items.append('flashlight')

                           elif start == 'kick the door':
                                   if door == 1:
                                           print('You have already done that.')
                                           print()
                                   else:
                                           print('You step back, aim, and BAM! The door flies off its hinges and slams onto the floor with a loud bang.')
                                           print()
                                           door = 1
                                           slam.play()

                           elif start == 'kick in the door':
                                   if door == 1:
                                           print('You have already done that.')
                                           print()
                                   else:
                                           print('You step back, aim, and BAM! The door flies off its hinges and slams onto the floor with a loud bang.')
                                           print()
                                           door = 1

                           elif start == 'kick door':
                                   if door == 1:
                                           print('You have already done that.')
                                           print()
                                   else:
                                           print('You step back, aim, and BAM! The door flies off its hinges and slams onto the floor with a loud bang.')
                                           print()
                                           door = 1


                           elif start == 'kick in door':
                                   if door == 1:
                                           print('You have already done that.')
                                           print()
                                   else:
                                           print('You step back, aim, and BAM! The door flies off its hinges and slams onto the floor with a loud bang.')
                                           print()
                                           door = 1

                           elif start == 'check items':
                              if items == []:
                                 print('You don\'t have any at the moment')
                                 print()
                              else:
                                 print(items)
                                 print()

                           elif start == 'items':
                              if items == []:
                                 print('You don\'t have any at the moment')
                                 print()
                              else:
                                 print(items)
                                 print()

                          

                           elif start == 'eat corn':
                              if 'corn' in items:
                                 print('You take the ear and gobble it down. Delicious')
                                 items.remove('corn')
                                 print()
                              else:
                                 print('You don\'t have any corn in your items')
                                 print()

                           elif start == 'throw corn':
                              if 'corn' in items:
                                 where = input('Where do you want to throw the corn? ').lower()
                                 
                                 if where == 'me':
                                    items.remove('corn')
                                    print('OW! Why would you do that to yourself?!')
                                    print()
                                    
                                 elif where == 'there':
                                    print('You throw the corn over there.')
                                    print()
                                    items.remove('corn')
                                    
                                 elif where == 'bird':
                                    print('You can\'t see any bird around.')
                                    print()

                                 elif where == 'you':
                                    print('Yeah, you wish you could hit this!')
                                    print()

                                 else:
                                    print('You can\'t do that.')
                                    print()

                              else:
                                 print('You don\'t have any corn to throw')
                                 print()
                             

                              

                           elif start == 'fag':
                              print(greet['fag'])
                              print()

                           elif start == 'faggot':
                              print(greet['fag'])
                              print()

                           elif start == 'you suck':
                              print(greet['ys'])
                              print()

                           elif start == 'whatever':
                              print(greet['mmm'])
                              print()

                           elif start == 'how are you':
                              print(greet['pg'])
                              print()

                           elif start == 'fagget':
                              print(greet['spell'])
                              print()

                           elif start == 'fagg':
                              print(greet['spell'])
                              print()

                           elif start == 'jump':
                              print('You jump up and down like a fool. You are now breathing heavily.')
                              print()

                           elif start == 'dance':
                              print(greet['dance'])
                              print()

                           elif start == 'sing':
                              print(greet['sing'])
                              print()

                           elif start == 'fuck you':
                              print(greet['fu'])
                              print()

                           elif start == 'smile':
                              print(greet['smile'])
                              print()

                           elif start == 'grin':
                              print(greet['grin'])
                              print()

                           elif start == 'bitch':
                              print(greet['ho'])
                              print()

                           elif start == 'i don\'t like you':
                              print(greet['idly'])
                              print()

                           elif start == 'i love you':
                              print(greet['ily'])
                              print()

                           elif start == 'hey':
                              print(greet['hey'])
                              print()

                           elif start == 'hi':
                              print(greet['heyt'])
                              print()

                           elif start == 'hello':
                              print(greet['hello'])
                              print()

                           elif start == 'dude':
                              print(greet['dude'])
                              print()

                           elif start == 'sweet':
                              print(greet['sweet'])
                              print()   

                           elif start == 'you':
                              print(greet['crank'])
                              print()   
                              
                           elif start == 'look around':
                              print(greet['la'])
                              print()

                           elif start == 'la':
                              print(greet['la'])
                              print()
                              
                           elif start == 'north':
                                   if door == 0:
                                           print('You can\'t go inside unless you find a way in.')
                                           print()
                                   elif door == 1:
                                           if 'flashlight' not in items:
                                                   print('You can\'t go in without a flashlight.')
                                                   print()
                                           else:
                                                    print('You head inside the house and you come into a living room.')
                                                    print()
                                                    place = ['livingroom']
                                                    house = 0

                           elif start == 'go north':
                                   if door == 0:
                                           print('You can\'t go inside unless you find a way in.')
                                           print()
                                   elif door == 1:
                                           if 'flashlight' not in items:
                                                   print('You can\'t go in without a flashlight.')
                                                   print()
                                           else:
                                                    print('You head inside the house and you come into a living room.')
                                                    print()
                                                    place = ['livingroom']
                                                    house = 0

                           elif start == 'west':
                              print(greet['west'])
                              print()

                           elif start == 'go west':
                              print(greet['west'])
                              print()

                           
                           elif start == 'damn':
                              print(greet['cuss'])
                              print()

                           elif start == 'you bastard':
                              print(greet['yb'])
                              print()

                           elif start == 'fuck':
                              print(greet['cuss'])
                              print()

                           elif start == 'shit':
                              print(greet['cuss'])
                              print()

                           

                           elif start == 'what\'s up':
                              print(greet['whatup'])
                              print()

                           else:
                                   print('I don\'t know the word(s): ' + start)
                                   print()

                






                





##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# place = ['livingroom']----------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['livingroom']:
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in the livingroom of the house. There is not much to look at except for an out-dated tv, an old, dirty couch, and an equally dirty coffee table full of water circles. There is a kitchen to the west and a hall to the north.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }


                LRMAP = '''
                ________________________________________________
                |                                               |
                |                                               |
                |                                               |
                |                                               |
                |                | |                            |
                |                | |                            |
                |                | |                            |
                |                | |                            |
                |                | |________                    |
                |                |    [TV]  |                   |
                |   _____________|          |                   |
                |  |                __[ ]__ |                   |
                |  |   KITCHEN      |couch| |                   |
                |  |______________{U}_______|                   |       
                |                 | |                           |
                |                HOUSE                          |
                |-----------------------------------------------|

                '''


                
                livingroom = 1
                lrmap = 1
                while livingroom == 1:

                    print('Livingroom')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      livingroom = 0
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()
                      

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                            

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'map':
                            print(LRMAP)

                    elif start == 'kitchen':
                            if memory1 == 0:
                                    
                                    print('You head into the kitchen almost remembering a distant memory. Something of a child singing while breakfast was being made.')
                                    print()
                                    place = ['kitchen']
                                    livingroom = 0
                                    memory1 = 1

                            else:
                                    print('You head into the kitchen. That memory really has you trying hard to remember something, anything, but to no avail.')
                                    print()
                                    place = ['kitchen']
                                    livingroom = 0
                                    


                    elif start == 'go back':
                            print('You head back to the porch.')
                            print()
                            place = ['house']
                            livingroom = 0

                    elif start == 'go south':
                            print('You head back to the porch.')
                            print()
                            place = ['house']
                            livingroom = 0

                    elif start == 'south':
                            print('You head back to the porch.')
                            print()
                            place = ['house']
                            livingroom = 0


                    
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('You are too scared to jump seeing as it could attract some undesired attention.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                      print(greet['la'])
                      print()

                    elif start == 'la':
                      print(greet['la'])
                      print()

                    elif start == 'north':
                            print('You head north to the hall.')
                            print()
                            livingroom = 0
                            place = ['hall']

                    elif start == 'go north':
                            print('You head north to the hall.')
                            print()
                            livingroom = 0
                            place = ['hall']
                            
                      
                    

                    elif start == 'west':
                      print('You head to the kitchen.')
                      print()
                      livingroom = 0
                      place = ['kitchen']
                      
                    elif start == 'go west':
                      print('You head to the kitchen.')
                      print()
                      livingroom = 0
                      place = ['kitchen']

                    elif start == 'east':
                            print('You cannot go east.')
                            print()

                    elif start == 'go east':
                            print('You can\'t go east.')
                            print()

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
                







##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################

# place = ['hall']----------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['hall']:
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in the middle of the hall. There is a door to your north, to the east, and to the west. The livingroom is to the south.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }


                


                
                hall = 1
                
                while hall == 1:

                    print('Hall')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      hall = 0
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()
                      

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                            

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'map':
                            if bathroommap == 1:
                                    if bedroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL) 
                                            else:

                                                    print(HALLBATHBED)
                                    elif studymap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    
                                                    print(HALLSTUDYBATH)
                                            
                                    else:
                                            print(HALLBATHROOM)
                                            
                            elif bedroommap == 1:
                                    if bathroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBATHBED)

                                    elif studymap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    print(HALLBEDSTUDY)
                                                    
                                    else:
                                            print(HALLBEDROOM)


                            elif studymap == 1:
                                    if bathroommap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLSTUDYBATH)

                                    elif bedroommap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBEDSTUDY)
                                    else:
                                            print(HALLSTUDY)
                                    
                            else:
                                    print(HALLBLANK)








                                                    

                    
                                    


                    elif start == 'go back':
                            print('You head back to the livingroom.')
                            print()
                            place = ['livingroom']
                            hall = 0

                    elif start == 'go south':
                            print('You head back to the livingroom.')
                            print()
                            place = ['livingroom']
                            hall = 0

                    elif start == 'south':
                            print('You head back to the livingroom.')
                            print()
                            place = ['livingroom']
                            hall = 0


                    
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('You are too scared to jump seeing as it could attract some undesired attention.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                      print(greet['la'])
                      print()

                    elif start == 'la':
                      print(greet['la'])
                      print()
                      
                    

                    elif start == 'west':
                            if bedroommap == 0:
                                    print('You head to the door to the west.')
                                    print()
                                    hall = 0
                                    place = ['bedroom']

                            else:
                                    print('You head to the bedroom.')
                                    print()
                                    hall = 0
                                    place = ['bedroom']
                                    
                      
                      
                    elif start == 'go west':
                      if bedroommap == 0:
                                    print('You head to the door to the west.')
                                    print()
                                    hall = 0
                                    place = ['bedroom']

                      else:
                                    print('You head to the bedroom.')
                                    print()
                                    hall = 0
                                    place = ['bedroom']

                    elif start == 'east':
                            if studymap == 0:
                                    print('You head to the door to the east.')
                                    print()
                                    hall = 0
                                    place = ['study']

                            else:
                                    print('You head to the study.')
                                    print()
                                    hall = 0
                                    place = ['study']

                    elif start == 'go east':
                            if studymap == 0:
                                    print('You head to the door to the east.')
                                    print()
                                    hall = 0
                                    place = ['study']

                            else:
                                    print('You head to the study.')
                                    print()
                                    hall = 0
                                    place = ['study']

                    elif start == 'north':
                            if bathroommap == 0:
                                    print('You head to the door to the north.')
                                    print()
                                    hall = 0
                                    place = ['bathroom']

                            else:
                                    print('You head to the bathroom.')
                                    print()
                                    hall = 0
                                    place = ['bathroom']

                    elif start == 'go north':
                            if bathroommap == 0:
                                    print('You head to the door to the north.')
                                    print()
                                    hall = 0
                                    place = ['bathroom']

                            else:
                                    print('You head to the bathroom.')
                                    print()
                                    hall = 0
                                    place = ['bathroom']
                                    
                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()

##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################

# place = ['bedroom']----------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['bedroom']:
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in the middle of a bedroom. You see an old, dirty bed, a night stand, and a small bookshelf. There is a window looking to the west of the house.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }


                


                
                bedroom = 1
                bedroommap = 1
                while bedroom == 1:

                    print('Bedroom')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      bedroom = 0
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()
                      

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                            

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'map':
                            if bathroommap == 1:
                                    if bedroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL) 
                                            else:

                                                    print(HALLBATHBED)
                                    elif studymap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    
                                                    print(HALLSTUDYBATH)
                                            
                                    else:
                                            print(HALLBATHROOM)
                                            
                            elif bedroommap == 1:
                                    if bathroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBATHBED)

                                    elif studymap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    print(HALLBEDSTUDY)
                                                    
                                    else:
                                            print(HALLBEDROOM)


                            elif studymap == 1:
                                    if bathroommap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLSTUDYBATH)

                                    elif bedroommap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBEDSTUDY)
                                    else:
                                            print(HALLSTUDY)
                                    
                            else:
                                    print(HALLBLANK)








                                                    

                    
                                    


                    elif start == 'go back':
                            print('You head back to the hall.')
                            print()
                            place = ['hall']
                            bedroom = 0

                    elif start == 'go south':
                            print('You can\'t go south from here.')
                            print()

                    elif start == 'south':
                            print('You can\'t go south from here.')
                            print()
                            


                    
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('You are too scared to jump seeing as it could attract some undesired attention.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()

                    elif start == 'take keys':
                            if whichroomhaskey == 1:
                                    if 'truck keys' not in items:
                                            print('You take the truck keys.')
                                            print()
                                            items.append('truck keys')
                                    else:
                                            print('You already have the truck keys.')
                                            print()

                            else:
                                    print('You don\'t see any truck keys.')
                                    print()

                    elif start == 'take truck keys':
                            if whichroomhaskey == 1:
                                    if 'truck keys' not in items:
                                            print('You take the truck keys.')
                                            print()
                                            items.append('truck keys')
                                    else:
                                            print('You already have the truck keys.')
                                            print()

                            else:
                                    print('You don\'t see any truck keys.')
                                    print()    
                      
                    elif start == 'look around':
                     if whichroomhaskey == 1:
                             if 'truck keys' not in items:
                                     print('You are in the middle of a bedroom. You see an old, dirty bed, a night stand, and a small bookshelf. There is also a set of truck keys on the night stand. There is a window looking to the west of the house.')
                                     print()

                             else:
                                    print('You are in the middle of a bedroom. You see an old, dirty bed, a night stand, and a small bookshelf. There is a window looking to the west of the house.')
                     else:
                             
                      print(greet['la'])
                      print()

                    elif start == 'la':
                      if whichroomhaskey == 1:
                             if 'truck keys' not in items:
                                     print('You are in the middle of a bedroom. You see an old, dirty bed, a night stand, and a small bookshelf. There is also a set of truck keys on the night stand. There is a window looking to the west of the house.')
                                     print()

                             else:
                                    print('You are in the middle of a bedroom. You see an old, dirty bed, a night stand, and a small bookshelf. There is a window looking to the west of the house.')
                      else:
                             
                       print(greet['la'])
                       print()
                      
                    

                    elif start == 'west':
                            
                                    print('You can\'t go west from here. The window is painted shut.')
                                    print()

                            
                                    
                      
                      
                    elif start == 'go west':
                              print('You can\'t go west from here. The window is painted shut.')
                              print()

                    elif start == 'east':
                          print('You head back to the hall.')
                          print()
                          bedroom = 0
                          place = ['hall']
                          
                    elif start == 'go east':
                          print('You head back to the hall.')
                          print()
                          bedroom = 0
                          place = ['hall']

                    elif start == 'north':
                           print('You can\'t go north from here.')
                           print()
                           
                    elif start == 'go north':
                           print('You can\'t go north from here.')
                           print()
                                    
                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()

##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################

# place = ['study']----------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['study']:
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in the middle of a study. The walls are lined with bookshelfs full of various interesting books. There is an old desk here with an office chair behind it.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }


                


                
                study = 1
                studymap = 1
                while study == 1:

                    print('Study')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      study = 0
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()
                      

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                            

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'map':
                            if bathroommap == 1:
                                    if bedroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL) 
                                            else:

                                                    print(HALLBATHBED)
                                    elif studymap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    
                                                    print(HALLSTUDYBATH)
                                            
                                    else:
                                            print(HALLBATHROOM)
                                            
                            elif bedroommap == 1:
                                    if bathroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBATHBED)

                                    elif studymap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    print(HALLBEDSTUDY)
                                                    
                                    else:
                                            print(HALLBEDROOM)


                            elif studymap == 1:
                                    if bathroommap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLSTUDYBATH)

                                    elif bedroommap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBEDSTUDY)
                                    else:
                                            print(HALLSTUDY)
                                    
                            else:
                                    print(HALLBLANK)








                                                    

                    
                                    


                    elif start == 'go back':
                            print('You head back to the hall.')
                            print()
                            place = ['hall']
                            study = 0

                    elif start == 'go south':
                            print('You can\'t go south from here.')
                            print()

                    elif start == 'south':
                            print('You can\'t go south from here.')
                            print()
                            


                    
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('You are too scared to jump seeing as it could attract some undesired attention.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'take keys':
                            if whichroomhaskey == 2:
                                    if 'truck keys' not in items:
                                            print('You take the truck keys.')
                                            print()
                                            items.append('truck keys')
                                    else:
                                            print('You already have the truck keys.')
                                            print()

                            else:
                                    print('You don\'t see any truck keys.')
                                    print()

                    elif start == 'take truck keys':
                            if whichroomhaskey == 2:
                                    if 'truck keys' not in items:
                                            print('You take the truck keys.')
                                            print()
                                            items.append('truck keys')
                                    else:
                                            print('You already have the truck keys.')
                                            print()

                            else:
                                    print('You don\'t see any truck keys.')
                                    print()    
                      
                    elif start == 'look around':
                     if whichroomhaskey == 2:
                             if 'truck keys' not in items:
                                     print('You are in the middle of a study. The walls are lined with bookshelfs full of various interesting books. There is an old desk with a set of truck keys on it with an office chair behind it.')
                                     print()

                             else:
                                     print('You are in the middle of a study. The walls are lined with bookshelfs full of various interesting books. There is an old desk here with an office chair behind it.')
                     else:
                             
                      print(greet['la'])
                      print()

                    elif start == 'la':
                      if whichroomhaskey == 2:
                             if 'truck keys' not in items:
                                     print('You are in the middle of a study. The walls are lined with bookshelfs full of various interesting books. There is an old desk with a set of truck keys on it with an office chair behind it.')
                                     print()

                             else:
                                     print('You are in the middle of a study. The walls are lined with bookshelfs full of various interesting books. There is an old desk here with an office chair behind it.')
                      else:
                             
                       print(greet['la'])
                       print()
                      
                    

                    elif start == 'east':
                            
                                    print('You can\'t go east from here.')
                                    print()

                            
                                    
                      
                      
                    elif start == 'go east':
                              print('You can\'t go east from here.')
                              print()

                    elif start == 'west':
                          print('You head back to the hall.')
                          print()
                          study = 0
                          place = ['hall']
                          
                    elif start == 'go west':
                          print('You head back to the hall.')
                          print()
                          study = 0
                          place = ['hall']

                    elif start == 'north':
                           print('You can\'t go north from here.')
                           print()
                           
                    elif start == 'go north':
                           print('You can\'t go north from here.')
                           print()
                                    
                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()

##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################

# place = ['bathroom']----------------------------------------------------------------------------------------------------------------------------------------
        
        elif place == ['bathroom']:
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in the bathroom. Even though it does not appear to have been used for quite a while it still has an awful stench inside of it. All that\'s in here is the usual bathroom stuff. The shower curtain is closed though.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }


                


                
                bathroom = 1
                bathroommap = 1
                while bathroom == 1:

                    print('Bathroom')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      bathroom = 0
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()
                      

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                            

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                    
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'map':
                            if bathroommap == 1:
                                    if bedroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL) 
                                            else:

                                                    print(HALLBATHBED)
                                    elif studymap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    
                                                    print(HALLSTUDYBATH)
                                            
                                    else:
                                            print(HALLBATHROOM)
                                            
                            elif bedroommap == 1:
                                    if bathroommap == 1:
                                            if studymap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBATHBED)

                                    elif studymap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)

                                            else:
                                                    print(HALLBEDSTUDY)
                                                    
                                    else:
                                            print(HALLBEDROOM)


                            elif studymap == 1:
                                    if bathroommap == 1:
                                            if bedroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLSTUDYBATH)

                                    elif bedroommap == 1:
                                            if bathroommap == 1:
                                                    print(HALLALL)
                                            else:
                                                    print(HALLBEDSTUDY)
                                    else:
                                            print(HALLSTUDY)
                                    
                            else:
                                    print(HALLBLANK)








                                                    

                    
                                    


                    elif start == 'go back':
                            print('You head back to the hall.')
                            print()
                            place = ['hall']
                            bathroom = 0

                    elif start == 'go south':
                            print('You head back to the hall.')
                            print()
                            place = ['hall']
                            bathroom = 0

                    elif start == 'south':
                            print('You head back to the hall.')
                            print()
                            place = ['hall']
                            bathroom = 0
                            


                    
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('You are too scared to jump seeing as it could attract some undesired attention.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()
                    elif start == 'close':
                            if shower == 0:
                                    print('It is already closed.')
                                    print()

                            else:
                                    print('You close the curtain.')
                                    print()
                                    shower = 0
                    elif start == 'close shower curtain':
                            if shower == 0:
                                    print('It is already closed.')
                                    print()

                            else:
                                    print('You close the curtain.')
                                    print()
                                    shower = 0
                                    
                    elif start == 'close shower':
                            if shower == 0:
                                    print('It is already closed.')
                                    print()

                            else:
                                    print('You close the curtain.')
                                    print()
                                    shower = 0
                                    
                    elif start == 'open shower curtain':
                            if shower == 0:
                                    print('You open the shower and to your horror, you see a women dead in a bathtub filled with blood. The women has apperently committed suicide due to huge gashes cut into her wrist.')
                                    print()
                                    shower = 1

                            else:
                                    print('The curtain is already open.')
                                    print()  
                    elif start == 'open':
                            if shower == 0:
                                    print('You open the shower and to your horror, you see a women dead in a bathtub filled with blood. The women has apperently committed suicide due to huge gashes cut into her wrist.')
                                    print()
                                    shower = 1

                            else:
                                    print('The curtain is already open.')
                                    print()
                    elif start == 'open shower':
                            if shower == 0:
                                    print('You open the shower and to your horror, you see a women dead in a bathtub filled with blood. The women has apperently committed suicide due to huge gashes cut into her wrist.')
                                    print()
                                    shower = 1

                            else:
                                    print('The curtain is already open.')
                                    print()
                                    
                      
                    elif start == 'take keys':
                            if whichroomhaskey == 3:
                                    if 'truck keys' not in items:
                                            print('You take the truck keys.')
                                            print()
                                            items.append('truck keys')
                                    else:
                                            print('You already have the truck keys.')
                                            print()

                            else:
                                    print('You don\'t see any truck keys.')
                                    print()

                    elif start == 'take truck keys':
                            if whichroomhaskey == 3:
                                    if 'truck keys' not in items:
                                            print('You take the truck keys.')
                                            print()
                                            items.append('truck keys')
                                    else:
                                            print('You already have the truck keys.')
                                            print()

                            else:
                                    print('You don\'t see any truck keys.')
                                    print()    
                      
                    elif start == 'look around':
                     if whichroomhaskey == 3:
                             if 'truck keys' not in items:
                                    if shower == 0:
                                            
                                     print('You are in the bathroom. Even though it does not appear to have been used for quite a while it still has an awful stench inside of it. All that\'s in here is the usual bathroom stuff. There is also a set of truck keys on the sink and the shower curtain is closed.')
                                     print()
                                    else:
                                       print('You are in the bathroom. There is a dead women who has apparently committed suicide in the tub. There is also a set of truck keys on the sink.')
 

                             else:
                                    if shower == 0:
                                             
                                        print('You are in the bathroom. Even though it does not appear to have been used for quite a while it still has an awful stench inside of it. All that\'s in here is the usual bathroom stuff. The shower curtain is closed though.')
                                    else:
                                        print('You are in the bathroom. There is a dead women who has apparently committed suicide in the tub. There is also a set of truck keys on the sink.')


                     else:
                        if shower == 0:
                                             
                                        print('You are in the bathroom. Even though it does not appear to have been used for quite a while it still has an awful stench inside of it. All that\'s in here is the usual bathroom stuff. The shower curtain is closed though.')
                        else:
                                        print('You are in the bathroom. There is a dead women who has apparently committed suicide in the tub.')

                                             
                             
                      

                    elif start == 'la':
                       if whichroomhaskey == 3:
                             if 'truck keys' not in items:
                                    if shower == 0:
                                            
                                     print('You are in the bathroom. Even though it does not appear to have been used for quite a while it still has an awful stench inside of it. All that\'s in here is the usual bathroom stuff. There is also a set of truck keys on the sink and the shower curtain is closed.')
                                     print()
                                    else:
                                       print('You are in the bathroom. There is a dead women who has apparently committed suicide in the tub. There is also a set of truck keys on the sink.')
 

                             else:
                                    if shower == 0:
                                             
                                        print('You are in the bathroom. Even though it does not appear to have been used for quite a while it still has an awful stench inside of it. All that\'s in here is the usual bathroom stuff. The shower curtain is closed though.')
                                    else:
                                        print('You are in the bathroom. There is a dead women who has apparently committed suicide in the tub. There is also a set of truck keys on the sink.')


                       else:
                        if shower == 0:
                                             
                                        print('You are in the bathroom. Even though it does not appear to have been used for quite a while it still has an awful stench inside of it. All that\'s in here is the usual bathroom stuff. The shower curtain is closed though.')
                        else:
                                        print('You are in the bathroom. There is a dead women who has apparently committed suicide in the tub.')

                      
                    

                    elif start == 'east':
                            
                                    print('You can\'t go east from here.')
                                    print()

                            
                                    
                      
                      
                    elif start == 'go east':
                              print('You can\'t go east from here.')
                              print()

                    elif start == 'west':
                          print('You can\'t go west from here.')
                          print()
                          
                    elif start == 'go west':
                          print('You can\'t go west from here.')
                          print()

                    elif start == 'north':
                           print('You can\'t go north from here.')
                           print()
                           
                    elif start == 'go north':
                           print('You can\'t go north from here.')
                           print()
                                    
                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()



###############################################################################################################################################################
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################        
###############################################################################################################################################################
                        
# place = ['kitchen']----------------------------------------------------------------------------------------------------------------------------------------
        

        elif place == ['kitchen']:
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in the kitchen of the house. There are the normal kitchen appliances like an oven, a refrigerator, a microwave, and a series of drawers and cabinets. There is also a table with what looks like mail on it. Perhaps you should "look".',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }


                LRMAP = '''
                ________________________________________________
                |                                               |
                |                                               |
                |                                               |
                |                                               |
                |                | |                            |
                |                | |                            |
                |                | |                            |
                |                | |                            |
                |                | |________                    |
                |                |    [TV]  |                   |
                |   _____________|          |                   |
                |  |                __[ ]__ |                   |
                |  |   KITCHEN      |couch| |                   |
                |  |______{U}_______________|                   |       
                |                 | |                           |
                |                HOUSE                          |
                |-----------------------------------------------|

                '''
                kitchen = 1
                while kitchen == 1:

                    print('Kitchen')
                    start = input('You: ').lower()
                    print()
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      kitchen = 0
                      
                      running = 0

                 

                    elif start == 'look':
                            print('What do you want to look at.')
                            lookat = input('...')
                            if lookat == 'table':
                                    if lookedattable == 0:
                                    
                                            print('You examine the table and start rifling through the various bills and junk mail when, suddenly, a letter catches your eye.')
                                            print()
                                            print('The letter reads as thus:')
                                            print(letter)
                                            print()
                                            lookedattable = 1

                                    else:
                                            print('You have looked the table over thoroughly and there is nothing more of importance. Unless you want another credit card or something.')
                                            print()

                            elif lookat == 'oven':
                                            if ovenopened == 0:
                                    
                                                    print('It is a dingy-looking oven that hasn\'t seemed to have been used for months. It is all covered in dust and grime. It can be opened though.')
                                                    print()

                                            else:
                                                    print('The oven is open and you see there is nothing inside.')

                            elif lookat == 'microwave':
                                    if microwaveopened == 0:
                                            
                                            print('It\'s a cheap microwave not big enough to fit a standard-sized plate. It can be opened.')
                                            print()

                                    else:
                                            print('The microwave is open and there is a plate inside of it wrapped in foil.')
                                            print()
                                            
                            elif lookat == 'refrigerator':
                                    if fridgeopened == 0:
                                            
                                            print('It is a white fridge with the freezer side to the left and the fridge side to the right. It can be opened.')
                                            print()

                                    else:
                                            print('There is an awful smell eminating from the open fridge. There power must have been off for quite some time because all of the food has spoiled!')
                                            print()

                            elif lookat == 'fridge':
                                    if fridgeopened == 0:
                                            
                                            print('It is a white fridge with the freezer side to the left and the fridge side to the right. It can be opened.')
                                            print()

                                    else:
                                            print('There is an awful smell eminating from the open fridge. There power must have been off for quite some time because all of the food has spoiled!')
                                            print()
                            
                                            

                            else:
                                    print('Perhaps writing it a different way would help. Remember no articles.')
                                    print()
                                    

                    elif start == 'look at oven':
                            if ovenopened == 0:
                                    
                                    print('It is a dingy-looking oven that hasn\'t seemed to have been used for months. It is all covered in dust and grime. It can be opened though.')
                                    print()

                            else:
                                    print('The oven is open and you see there is nothing inside.')
                                    

                    
                            
                    elif start == 'table':
                            if lookedattable == 0:
                                    
                                    print('You examine the table and start rifling through the various bills and junk mail when, suddenly, a letter catches your eye.')
                                    print()
                                    print('The letter reads as thus:')
                                    print(letter)
                                    print()
                                    lookedattable = 1

                            else:
                                    print('You have looked the table over thoroughly and there is nothing more of importance. Unless you want another credit card or something.')
                                    print()    
                    elif start == 'look at table':
                            if lookedattable == 0:
                                    
                                    print('You examine the table and start rifling through the various bills and junk mail when, suddenly, a letter catches your eye.')
                                    print()
                                    print('The letter reads as thus:')
                                    print(letter)
                                    print()
                                    lookedattable = 1

                            else:
                                    print('You have looked the table over thoroughly and there is nothing more of importance. Unless you want another credit card or something.')
                                    print()

                    elif start == 'look at fridge':
                            if fridgeopened == 0:
                                            
                                            print('It is a white fridge with the freezer side to the left and the fridge side to the right. It can be opened.')
                                            print()

                            else:
                                            print('There is an awful smell eminating from the open fridge. There power must have been off for quite some time because all of the food has spoiled!')
                                            print()

                    elif start == 'look at refrigerator':
                            if fridgeopened == 0:
                                            
                                            print('It is a white fridge with the freezer side to the left and the fridge side to the right. It can be opened.')
                                            print()

                            else:
                                            print('There is an awful smell eminating from the open fridge. There power must have been off for quite some time because all of the food has spoiled!')
                                            print()

                    elif start == 'look at microwave':
                            if microwaveopened == 0:
                                            
                                            print('It\'s a cheap microwave not big enough to fit a standard-sized plate. It can be opened.')
                                            print()

                            else:
                                            print('The microwave is open and there is a plate inside of it wrapped in foil.')
                                            print()
                            

                    elif start == 'open oven':
                            if ovenopened == 0:
                                    print('You open the oven.')
                                    print()
                                    ovenopened = 1

                            else:
                                    print('It is already open.')

                    elif start == 'open fridge':
                            if fridgeopened == 0:
                                    print('You open the fridge.')
                                    print()
                                    fridgeopened = 1

                            else:
                                    print('It is already open.')

                    elif start == 'open refrigerator':
                            if fridgeopened == 0:
                                    print('You open the fridge.')
                                    print()
                                    fridgeopened = 1

                            else:
                                    print('It is already open.')

                    elif start == 'open microwave':
                            if microwaveopened == 0:
                                    print('You open the microwave.')
                                    print()
                                    microwaveopened = 1

                            else:
                                    print('It is already open.')


                    elif start == 'close oven':
                            if ovenopened == 1:
                                    print('You close the oven.')
                                    print()
                                    ovenopened = 0

                            else:
                                    print('It is already closed.')

                    elif start == 'close fridge':
                            if fridgeopened == 1:
                                    print('You close the fridge.')
                                    print()
                                    fridgeopened = 0

                            else:
                                    print('It is already closed.')

                    elif start == 'close refrigerator':
                            if fridgeopened == 1:
                                    print('You close the fridge.')
                                    print()
                                    fridgeopened = 0

                            else:
                                    print('It is already closed.')

                    elif start == 'close microwave':
                            if microwaveopened == 1:
                                    print('You close the microwave.')
                                    print()
                                    microwaveopened = 0

                            else:
                                    print('It is already closed.')


                    elif start == 'read letter':
                            print(letter)
                            print()

                                    
                    elif start == 'take letter':
                            if 'letter' in items:
                                    print('You already have the letter.')
                                    print()
                            else:
                                    print('Letter taken.')
                                    items.append('letter')
                                    print()

                    elif start == 'take the letter':
                            if 'letter' in items:
                                    print('You already have the letter.')
                                    print()
                            else:
                                    print('Letter taken.')
                                    items.append('letter')
                                    print()
                            
                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'map':
                            print(LRMAP)

                    
                                    


                    elif start == 'go back':
                            print('You head back into the livingroom.')
                            print()
                            place = ['livingroom']
                            kitchen = 0

                    elif start == 'go south':
                            print('You can\'t head south from here.')
                            print()
                           
                    elif start == 'south':
                            print('You can\'t head south from here.')
                            print()

                    elif start == 'east':
                            print('You head back to the livingroom.')
                            print()
                            place = ['livingroom']
                            kitchen = 0

                    elif start == 'go east':
                            print('You head back to the livingroom.')
                            print()
                            place = ['livingroom']
                            kitchen = 0

                    elif start == 'west':
                            print('You head back into the livingroom.')
                            print()
                            place = ['livingroom']
                            kitchen = 0

                    elif start == 'go west':
                            print('You head back into the livingroom.')
                            print()
                            place = ['livingroom']
                            kitchen = 0
                          


                    
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('You will do no such thing. There could be someone crazy lurking about.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                      print(greet['la'])
                      print()

                    elif start == 'la':
                      print(greet['la'])
                      print()
                      
                    

                    

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()

                        














































##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# 5: place = ['inbarn']-----------------------------------------------------------------------------------------------------------------------------------------

        elif place == ['inbarn']:
                greet = { 'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are inside of the barn. There are stalls here and appears to have been used recently. There is a ladder leading to a loft and there is a machete lying on the ground.',
                     'north': 'You walk out from the field to see a small house with a red worn barn to the left of it. There is an overbearing smell of ammonia in the air. In the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making a fool of yourself. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }
                
                

                        
                inbarn = 1
                while inbarn == 1:

                    print('Inside Barn')    
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')

                      
                      
                      place = ['20']
                      inbarn = 0
                     
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()


                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
                            

                                    
                      
                    elif start == 'north':
                            print('You head up the ladder to the loft.')
                            print()
                            
                            place = ['loft']
                            inbarn = 0
                            

                    elif start == 'go north':
                            print('You head up the ladder to the loft.')
                            print()
                            place = ['loft']
                            inbarn = 0

                    elif start == 'loft':
                            print('You head up the ladder to the loft.')
                            print()
                            place = ['loft']
                            inbarn = 0

                    elif start == 'go to the loft':
                            print('You head up the ladder to the loft.')
                            print()
                            place = ['loft']
                            inbarn = 0


                    elif start == 'go up':
                            print('You head up the ladder to the loft.')
                            print()
                            place = ['loft']
                            inbarn = 0

                    elif start == 'go up ladder':
                            print('You head up the ladder to the loft.')
                            print()
                            place = ['loft']
                            inbarn = 0

                    elif start == 'go to loft':
                            print('You head up the ladder to the loft.')
                            print()
                            place = ['loft']
                            inbarn = 0
                            
                     

                                   
                        
                        
                     
                        
                
                        
                    
                        
                        

                                   
                        
                    
                    elif start == 'east':
                        print('You can\'t go east from here.')
                        print()
                        
                       

                    elif start == 'go east':
                        print('You can\'t go east from here.')
                        print()
                        
                       
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'take machete':
                            if 'machete' not in items:
                                    
                         
                                 items.append('machete')
                      
                                 print('Machete taken.')
                                 print()
                                 

                            else:
                                    print('You already have the machete.')
                                    print()
                                

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print(greet['jump'])
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                            if 'machete' in items:
                                greet['la'] = 'You are inside of the barn. You see a ladder leading to a loft. There are stalls here and appears to have been used recently. There is a foul odor lingering in the air.'
                                print(greet['la'])
                                print()

                            else:
                                greet['la'] = 'You are inside of the barn. There are stalls here and appears to have been used recently. There is a ladder leading to a loft and there is a machete lying on the ground.'
                                print(greet['la'])
                                print() 
                      

                    elif start == 'la':
                            if 'machete' in items:
                                greet['la'] = 'You are inside of the barn. You see a ladder leading to a loft. There are stalls here and appears to have been used recently. There is a foul oder lingering in the air.'
                                print(greet['la'])
                                print()

                            else:
                                greet['la'] = 'You are inside of the barn. There are stalls here and appears to have been used recently. There is a ladder leading to a loft and there is a machete lying on the ground.'
                                print(greet['la'])
                                print()                
                      
                    elif start == 'south':
                      print('You head back in front of the barn.')
                      print()
                      place = ['barn']
                      inbarn = 0

                    elif start == 'go south':
                      print('You head back in front of the barn.')
                      print()
                      place = ['barn']
                      inbarn = 0
                      
                    elif start == 'go back':
                      print('You head back in front of the barn.')
                      print()
                      place = ['barn']
                      inbarn = 0
                      

                    elif start == 'west':
                      print(greet['west'])
                      print()

                    elif start == 'go west':
                      print(greet['west'])
                      print()

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()














##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# place = ['loft']------------------------------------------------------------------------------------------------------------------------------------------------
                        
        elif place == ['loft']:



                greet = { 'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are inside the loft of the barn. There is a "bed" made of hay with an old lantern and a note next to it. Uh-oh, you can see a little bit of blood on the floor.',
                     'north': 'You walk out from the field to see a small house with a red worn barn to the left of it. There is an overbearing smell of ammonia in the air. In the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making a fool of yourself. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }
                
                

                        
                loft = 1
                while loft == 1:

                    print('Loft')   
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')

                      
                      
                      place = ['20']
                      loft = 0
                     
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()


                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                                            
                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'read barn note':
                            
                                    print('''I have been forced to stay in this barn for the past 2 days since I cannot find a way into the house. My rations are getting lowand I will soon have to find some more. I can't sleep at night because of this awful howling I keep hearing in the distance.I pray every night it doesn't get closer. I\'m exhausted. I haven't gone out much because of it, but I am going to have to soon. If anyone finds this note, my name is Daniel Crosby. I lived in Sandusky, Ohio before all of this. I was an accountant. Tell Trish Crosby I love her.''')
                                    print()
                                    print('You think to yourself: Whoa, what in the world is going on around here? I heard that same howling outside. I wonder where he is now.')
                                    print()
                           

                    elif start == 'read note':
                            print(barnnote)
                            print()

                            print('You think to yourself: Whoa, what in the world is going on around here? I heard that same howling outside. I wonder where he is now.')
                            print()

                    elif start == 'read':
                            print('What do you want to read?')
                            what = input().lower()
                            if what == 'note':
                                    
                            
                                    print(barnnote)

                                    print('You think to yourself: Whoa, what in the world is going on around here? I heard that same howling outside. I wonder where he is now.')
                                    print()
                            elif what == 'the note':
                                    print(barnnote)

                                    print('You think to yourself: Whoa, what in the world is going on around here? I heard that same howling outside. I wonder where he is now.')
                                    print()

                            elif what == 'that note':
                                    print(barnnote)

                                    print('You think to yourself: Whoa, what in the world is going on around here? I heard that same howling outside. I wonder where he is now.')
                                    print()
                                    
                                    

                            else:
                                    print('Please explain to me how you would do that.')
                                    print()

                    

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
                            

                                    
                      
                    elif start == 'north':
                            print('You can\'t go north from here.')
                            print()
                            
                            
                            

                    elif start == 'go north':
                            print('You can\'t go north from here.')
                            print()
                           
              
                    
                    elif start == 'east':
                        print('You can\'t go east from here.')
                        print()
                        
                       

                    elif start == 'go east':
                        print('You can\'t go east from here.')
                        print()
                        
                       
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print(greet['jump'])
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()

                    elif start == 'take old lantern':
                                  print('You pick it up but it\'s busted and won\'t light. You decide not to take it.')
                                  print()

                    elif start == 'take lantern':
                                  print('You pick it up but it\'s busted and won\'t light. You decide not to take it.')
                                  print()

                    elif start == 'take note':
                            if 'barn note' not in items:
                                    
                                          print('You take the barn note.')
                                          print()
                                          items.append('barn note')

                            else:
                                    print('You already have the note.')
                                    print()
                                  

                                  
                      
                    elif start == 'look around':
                            if 'barn note' in items:
                                greet['la'] = 'You are inside the loft of the barn. You see an old lantern next to a bed made of hay. You can see a little blood on the floor.'
 
                                print(greet['la'])
                                print()

                            else:
                                greet['la'] = 'You are inside the loft of the barn. You see a note next to an old lantern next to a bed made of hay. You can see a little blood on the floor.'

                                print(greet['la'])
                                print() 
                      

                    elif start == 'la':
                            if 'barn note' in items:
                                greet['la'] = 'You are inside the loft of the barn. You see an old lantern next to a bed made of hay. You can see a little blood on the floor.'

                                print(greet['la'])
                                print()

                            else:
                                greet['la'] = 'You are inside the loft of the barn. You see a note next to an old lantern next to a bed made of hay. You can see a little blood on the floor.'
                                print(greet['la'])
                                print()                
                      
                    elif start == 'south':
                      print('You head back down the ladder into the barn.')
                      print()
                      place = ['inbarn']
                      loft = 0

                    elif start == 'go south':
                      print('You head back down the ladder into the barn.')
                      print()
                      place = ['inbarn']
                      loft = 0
                      
                    elif start == 'go back':
                      print('You head back down the ladder into the barn.')
                      print()
                      place = ['inbarn']
                      loft = 0
                      

                    elif start == 'west':
                      print(greet['west'])
                      print()

                    elif start == 'go west':
                      print(greet['west'])
                      print()

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    elif start == 'field':
                      print(greet['field'])
                      print()

                    elif start == 'look at field':
                      print(greet['field'])
                      print()

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()













##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# place = ['fronthouse']-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


        elif place == ['fronthouse']:

                mapfront = 1

                

 
                
                greet = { 'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in front of the house. You see a truck that looks old and worn but possibly usable, the trail to the right of the house to the east, and a trail leading north. There is also an old road but it seems as if a howling sound is coming from that way and you will not go without a vehicle of some kind.',
                     'north': 'You walk out from the field to see a small house with a red worn barn to the left of it. There is an overbearing smell of ammonia in the air. In the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making a fool of yourself. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }

                fronthouse = 1
                while fronthouse == 1:

                    if mightbedead == 1:
                            randomattack == random.randint(1,10)
                            if randomattack == 1:
                                    print('Oh no! The man with the severed arm is back!')
                                    print('press enter')
                                    input()
                                    print('What are you going to do?')
                                    whattodo = input('"run" or "fight"')
                                    if whattodo == 'run':
                                            rand = random.randint(1,2)
                                            if rand == 1:
                                                    print('The man runs after you but slips on something, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('As he falls the man lunges forward and lands directly on his neck.')
                                                    print('press enter')
                                                    input()
                                                    print('There is no need to check again or to double tap. The man is very dead.')
                                                    print()
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinfronthouse = 1
                                            else:
                                                    print('The man runs after you but slips on something, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('The man falls directly on his face and is stunned.')
                                                    print('press enter')
                                                    input()
                                                    print('You seize the opportunity and quickly jump up and down on his head, flattening him into the ground. The man is very dead now. Good job.')
                                                    print()    
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinfronthouse = 1

                                    elif whattodo == 'fight':
                                            random = random.randint(1,2)
                                            if random == 1:
                                                    print('You start to think which weapon you are going to use but there is no time; the man lunges forward.')
                                                    print('press enter')
                                                    input()
                                                    print('You dodge and land a punch square on his jaw, causing him to reel backward and fall over.')
                                                    print('press enter')
                                                    input()
                                                    print('HA! What a bit of luck. It seems the man has fallen onto an up-turn pitchfork. It has impaled the man in the chest and he is dying.')
                                                    print('press enter')
                                                    input()
                                                    print('You step on his chest making the spikes penetrate deeper into the mans body. He has died.')
                                                    print()
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinfronthouse = 1
                                            else:
                                                   print('You start to think which weapon you are going to use but there is not time; the man leaps forward.')
                                                   print('press enter')
                                                   input()
                                                   print('You try to dodge but he lands on top of you pinning you down growling and drooling in your face.')
                                                   print('press enter')
                                                   input()
                                                   print('You must decide now! Between two options: option "1" or option "2"')
                                                   oneortwo = input('"1" or "2"')
                                                   if oneortwo == '1':
                                                           print('I\'m so sorry, but your attempt to break free has ended up with the man sinking his teeth into your neck and pulling. You are quite dead. Sorry.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           fronthouse = 0
                                                           
                                                   elif oneortwo == 2:
                                                           print('Yes! Your barrel roll sends the man flying off of you and down the road.')
                                                           print('You cannot see him but you hear his footsteps getting more and more distant.')
                                                           print()

                                                   else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           fronthouse = 0

                                                           
                                    else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           fronthouse = 0
                                            
                    else:
                            None    

                    print('Front of the House')
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      fronthouse = 0
                      
                      running = 0

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'truck':
                            if 'truck keys' in items:
                                    print('You unlock the truck with the keys and get inside.')
                                    print()
                                    fronthouse = 0
                                    place = ['truck']

                            else:
                                    print('The truck is locked. You need a set of keys to get inside.')
                                    print()
                                    
                            
                    

                    elif start == 'get in truck':
                            if 'truck keys' in items:
                                    print('You unlock the truck with the keys and get inside.')
                                    print()
                                    fronthouse = 0
                                    place = ['truck']

                            else:
                                    print('The truck is locked. You need a set of keys to get inside.')
                                    print()

                    elif start == 'open truck':
                            if 'truck keys' in items:
                                    print('You unlock the truck with the keys and get inside.')
                                    print()
                                    fronthouse = 0
                                    place = ['truck']

                            else:
                                    print('The truck is locked. You need a set of keys to get inside.')
                                    print()
                                    
                    elif start == 'get inside truck':
                            if 'truck keys' in items:
                                    print('You unlock the truck with the keys and get inside.')
                                    print()
                                    fronthouse = 0
                                    place = ['truck']

                            else:
                                    print('The truck is locked. You need a set of keys to get inside.')
                                    print()
                                    
                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                                            
                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'south':
                            print('You head back to the right of the house.')
                            print()
                            fronthouse = 0
                            place = ['yardr']

                    elif start == 'go south':
                            print('You head back to the right of the house.')
                            print()
                            fronthouse = 0
                            place = ['yardr']

                    elif start == 'north':
                            print('You head up to the north.')
                            print()
                            fronthouse = 0
                            place = ['river']

                    elif start == 'go north':
                            print('You head north.')
                            print()
                            fronthouse = 0
                            place = ['river']

                    elif start == 'east':
                            print('You can\'t go east from here. Not without a vehicle of some sort.')
                            print()

                    elif start == 'go east':
                            print('You can\'t go east from here. Not without a vehicle of some kind.')
                            print()

                    elif start == 'west':
                            print('You can\'t go west from here.')
                            print()

                    elif start == 'go west':
                            print('You can\'t go west from here.')
                            print()

                    

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                    elif start == 'go to barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    fronthouse = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                    elif start == 'barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    fronthouse = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                      
                      
                    elif start == 'go to shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    fronthouse = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()

                    elif start == 'shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    fronthouse = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()
                     
                      

                    elif start == 'go to house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    fronthouse = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()
                                   
                    elif start == 'house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    fronthouse = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()





                    elif start == 'go to the house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    fronthouse = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
             
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('Nope. This time you refuse to jump. Who knows what could be lurking around out here.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                     if deadinfronthouse == 0:
                             
                      print(greet['la'])
                      print()
                     else:
                             print('You are in front of the house. You see a truck that looks old and worn but possibly usable, the trail to the right of the house to the east, and a trail leading north. There is also an old road but it seems as if a howling sound is coming from that way and you will not go without a vehicle of some kind. The man\'s body also is lying here.')
                             print()

                               

                    elif start == 'la':
                      if deadinfronthouse == 0:
                             
                       print(greet['la'])
                       print()
                      else:
                             print('You are in front of the house. You see a truck that looks old and worn but possibly usable, the trail to the right of the house to the east, and a trail leading north. There is also an old road but it seems as if a howling sound is coming from that way and you will not go without a vehicle of some kind. The man\'s body also is lying here.')
                             print()
                      
                    

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
                        

                








##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# place = ['inshed']---------------------------------------------------------------------------------------------------------------------------------------------------

        elif place == ['inshed']:

                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are inside the old shed. The walls are extremely dirty with various tools hanging on them. The only thing else you can see here is a chair next to a work bench and an old piano. There is sheet music here.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }

                

                inshed = 1
                while inshed == 1:

                    print('Inside the Shed')
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      inshed = 0
                      
                      running = 0

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'take tools':
                            if toolchoice == 0:
                                    
                                    print('You look at the various tools and decide upon a hammer, but to your chagrin, every tool has been bolted to the wall. How strange!')
                                    print()
                                    toolchoice = 1

                            else:
                                    print('You have already tried that but the tools are bolted to the wall.')
                                    print()

                    elif start == 'read':
                            if inshedmemory == 0:
                                print('You look at the sheet and see that it is "Moonlight Sonata". A flood of feelings comes rushing to you. You can almost remember some sweet memory from your past but it illudes you. You do, however, remember that you can play the piano.')
                                inshedmemory = 1

                            else:
                                    print('It is "Moonlight Sonata". You can remember playing this.')
                                    print()

                    elif start == 'sheet music':
                            if inshedmemory == 0:
                                print('You look at the sheet and see that it is "Moonlight Sonata". A flood of feelings comes rushing to you. You can almost remember some sweet memory from your past but it illudes you. You do, however, remember that you can play the piano.')
                                inshedmemory = 1

                            else:
                                    print('It is "Moonlight Sonata". You can remember playing this.')
                                    print()

                    elif start == 'read the sheet music':
                            if inshedmemory == 0:
                                print('You look at the sheet and see that it is "Moonlight Sonata". A flood of feelings comes rushing to you. You can almost remember some sweet memory from your past but it illudes you. You do, however, remember that you can play the piano.')
                                inshedmemory = 1

                            else:
                                    print('It is "Moonlight Sonata". You can remember playing this.')
                                    print()

                    elif start == 'read sheet music':
                            if inshedmemory == 0:
                                print('You look at the sheet and see that it is "Moonlight Sonata". A flood of feelings comes rushing to you. You can almost remember some sweet memory from your past but it illudes you. You do, however, remember that you can play the piano.')
                                inshedmemory = 1

                            else:
                                    print('It is "Moonlight Sonata". You can remember playing this.')
                                    print()

                    elif start == 'music':
                            if inshedmemory == 0:
                                print('You look at the sheet and see that it is "Moonlight Sonata". A flood of feelings comes rushing to you. You can almost remember some sweet memory from your past but it illudes you. You do, however, remember that you can play the piano.')
                                inshedmemory = 1

                            else:
                                    print('It is "Moonlight Sonata". You can remember playing this.')
                                    print()

                    elif start == 'read music':
                            if inshedmemory == 0:
                                print('You look at the sheet and see that it is "Moonlight Sonata". A flood of feelings comes rushing to you. You can almost remember some sweet memory from your past but it illudes you. You do, however, remember that you can play the piano.')
                                inshedmemory = 1

                            else:
                                    print('It is "Moonlight Sonata". You can remember playing this.')
                                    print()

                    elif start == 'read the music':
                            if inshedmemory == 0:
                                print('You look at the sheet and see that it is "Moonlight Sonata". A flood of feelings comes rushing to you. You can almost remember some sweet memory from your past but it illudes you. You do, however, remember that you can play the piano.')
                                inshedmemory = 1

                            else:
                                    print('It is "Moonlight Sonata". You can remember playing this.')
                                    print()

                    elif start == 'play':
                            if playedpiano == 0:
                                    if inshedmemory == 1:
                                            
                                    
                                            print('You begin to play the haunting melody. Joyfull sorrow fills the room as you continue to hit every note flawlessly. You suddenly realize that while you were playing, a door has opened in front of you, to the east.')
                                            print()
                                            playedpiano = 1

                                    else:
                                            print('You don\'t know if you can play the piano. You just can\'t remember. Maybe if you saw some sheet music or something...')
                                            print()

                            else:
                                    print('You have already played and you do not feel like playing again.')
                                    print()

                    elif start == 'play piano':
                            if playedpiano == 0:
                                    if inshedmemory == 1:
                                            
                                    
                                            print('You begin to play the haunting melody. Joyfull sorrow fills the room as you continue to hit every note flawlessly. You suddenly realize that while you were playing, a door has opened in front of you, to the east.')
                                            print()
                                            playedpiano = 1

                                    else:
                                            print('You don\'t know if you can play the piano. You just can\'t remember. Maybe if you saw some sheet music or something...')
                                            print()

                            else:
                                    print('You have already played and you do not feel like playing again.')
                                    print()

                    elif start == 'play the piano':
                            if playedpiano == 0:
                                    if inshedmemory == 1:
                                            
                                    
                                            print('You begin to play the haunting melody. Joyfull sorrow fills the room as you continue to hit every note flawlessly. You suddenly realize that while you were playing, a door has opened in front of you, to the east.')
                                            print()
                                            playedpiano = 1

                                    else:
                                            print('You don\'t know if you can play the piano. You just can\'t remember. Maybe if you saw some sheet music or something...')
                                            print()

                            else:
                                    print('You have already played and you do not feel like playing again.')
                                    print()

                    elif start == 'play music':
                            if playedpiano == 0:
                                    if inshedmemory == 1:
                                            
                                    
                                            print('You begin to play the haunting melody. Joyfull sorrow fills the room as you continue to hit every note flawlessly. You suddenly realize that while you were playing, a door has opened in front of you, to the east.')
                                            print()
                                            playedpiano = 1

                                    else:
                                            print('You don\'t know if you can play the piano. You just can\'t remember. Maybe if you saw some sheet music or something...')
                                            print()

                            else:
                                    print('You have already played and you do not feel like playing again.')
                                    print()


                    elif start == 'play the music':
                            if playedpiano == 0:
                                    if inshedmemory == 1:
                                            
                                    
                                            print('You begin to play the haunting melody. Joyfull sorrow fills the room as you continue to hit every note flawlessly. You suddenly realize that while you were playing, a door has opened in front of you, to the east.')
                                            print()
                                            playedpiano = 1

                                    else:
                                            print('You don\'t know if you can play the piano. You just can\'t remember. Maybe if you saw some sheet music or something...')
                                            print()

                            else:
                                    print('You have already played and you do not feel like playing again.')
                                    print()

                    elif start == 'play the sheet music':
                            if playedpiano == 0:
                                    if inshedmemory == 1:
                                            
                                    
                                            print('You begin to play the haunting melody. Joyfull sorrow fills the room as you continue to hit every note flawlessly. You suddenly realize that while you were playing, a door has opened in front of you, to the east.')
                                            print()
                                            playedpiano = 1

                                    else:
                                            print('You don\'t know if you can play the piano. You just can\'t remember. Maybe if you saw some sheet music or something...')
                                            print()

                            else:
                                    print('You have already played and you do not feel like playing again.')
                                    print()

                    elif start == 'play sheet music':
                            if playedpiano == 0:
                                    if inshedmemory == 1:
                                            
                                    
                                            print('You begin to play the haunting melody. Joyfull sorrow fills the room as you continue to hit every note flawlessly. You suddenly realize that while you were playing, a door has opened in front of you, to the east.')
                                            print()
                                            playedpiano = 1

                                    else:
                                            print('You don\'t know if you can play the piano. You just can\'t remember. Maybe if you saw some sheet music or something...')
                                            print()

                            else:
                                    print('You have already played and you do not feel like playing again.')
                                    print()
                            

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'east':
                            if playedpiano == 0:
                                    
                                    print('You can\'t go east from here.')

                            else:
                                    print('You head through the secret door to the east of the shed and follow a path.')
                                    print()
                                    inshed = 0
                                    place = ['pond']
                                    

                    elif start == 'go east':
                            if playedpiano == 0:
                                    
                                    print('You can\'t go east from here.')

                            else:
                                    print('You head through the secret door to the east of the shed and follow a path.')
                                    print()
                                    inshed = 0
                                    place = ['pond']
                                    
                         

                    
                          

                    elif start == 'north':
                            print('You can\'t go north from here.')
                           

                    elif start == 'go north':
                            print('You can\'t go north from here.')
                            

                    elif start == 'west':
                            print('You head back in front of the shed.')
                            print()
                            inshed = 0
                            place = ['shed']

                    elif start == 'go west':
                            print('You head back in front of the shed.')
                            print()
                            inshed = 0
                            place = ['shed']


                    elif start == 'go back':
                            print('You head back in front of the shed.')
                            print()
                            inshed = 0
                            place = ['shed']

                    elif start == 'back':
                            print('You head back in front of the shed.')
                            print()
                            inshed = 0
                            place = ['shed']
                            

                    elif start == 'south':
                            print('You can\'t go south from here.')
                            print()

                    elif start == 'go south':
                            print('You can\'t go south from here.')
                            print()

                    

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                    elif start == 'go to barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    field = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                    elif start == 'barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    field = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                      
                      
                    elif start == 'go to shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    field = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()

                    elif start == 'shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    field = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()
                     
                      

                    elif start == 'go to house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    field = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()
                                   
                    elif start == 'house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    field = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()





                    elif start == 'go to the house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    field = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
             
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('Hell no! You could be attacked at any moment. There\'s severed arms around here!')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                      if playedpiano == 1:
                        greet['la'] = 'You are inside the old shed. The walls are extremely dirty with various tools hanging on them. You can see a chair next to an old, dirty work bench, the piano you played, and the secret passage to the east.'
                        print(greet['la'])
                        print()
                        
                      else:
                        greet['la'] = 'You are inside the old shed. The walls are extremely dirty with various tools hanging on them. The only thing else you can see here is a chair next to a work bench and an old piano. There is sheet music here.'
                        print(greet['la'])
                        print()
                        
                    elif start == 'la':
                      if playedpiano == 1:
                        greet['la'] = 'You are inside the old shed. The walls are extremely dirty with various tools hanging on them. You can see a chair next to an old, dirty work bench, the piano you played, and the secret passage to the east.'
                        print(greet['la'])
                        print()
                        
                      else:
                        greet['la'] = 'You are inside the old shed. The walls are extremely dirty with various tools hanging on them. The only thing else you can see here is a chair next to a work bench and an old piano. There is sheet music here.'
                        print(greet['la'])
                        print()
                      
                    

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
                        









##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################






# place = ['pond']

        elif place == ['pond']:

                mapofpond = 1

                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in front of a small, hidden pond. There is a rickety old boat next to you and across the pond you can see an island.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }

                pond = 1
                while pond == 1:
                    if mightbedead == 1:
                            randomattack == random.randint(1,10)
                            if randomattack == 1:
                                    print('Oh no! The man with the severed arm is back!')
                                    print('press enter')
                                    input()
                                    print('What are you going to do?')
                                    whattodo = input('"run" or "fight"')
                                    if whattodo == 'run':
                                            rand = random.randint(1,2)
                                            if rand == 1:
                                                    print('The man runs after you but slips on something, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('As he falls the man lunges forward and lands directly on his neck.')
                                                    print('press enter')
                                                    input()
                                                    print('There is no need to check again or to double tap. The man is very dead.')
                                                    print('For some reason, you kick his body in the water and watch him float away. All of a sudden a pair of huge jaws lunges from the water and snatches the body.')
                                                    print('Good thing you didn\'t swim across.')
                                                    mightbedead = 0
                                                    dead = 1
                                                    
                                            else:
                                                    print('The man runs after you but slips on an something, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('The man falls directly on his face and is stunned.')
                                                    print('press enter')
                                                    input()
                                                    print('You seize the opportunity and quickly jump up and down on his head, flattening him into the ground. The man is very dead now. Good job.')
                                                    print()    
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinpond = 1
                                                    

                                    elif whattodo == 'fight':
                                            random = random.randint(1,2)
                                            if random == 1:
                                                    print('You start to think which weapon you are going to use but there is no time; the man lunges forward.')
                                                    print('press enter')
                                                    input()
                                                    print('You dodge and land a punch square on his jaw, causing him to reel backward and fall over.')
                                                    print('press enter')
                                                    input()
                                                    print('HA! What a bit of luck. It seems the man has fallen onto an up-turn pitchfork. It has impaled the man in the chest and he is dying.')
                                                    print('press enter')
                                                    input()
                                                    print('You step on his chest making the spikes penetrate deeper into the mans body. He has died.')
                                                    print()
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinpond = 1
                                                    
                                            else:
                                                   print('You start to think which weapon you are going to use but there is not time; the man leaps forward.')
                                                   print('press enter')
                                                   input()
                                                   print('You try to dodge but he lands on top of you pinning you down growling and drooling in your face.')
                                                   print('press enter')
                                                   input()
                                                   print('You must decide now! Between two options: option "1" or option "2"')
                                                   oneortwo = input('"1" or "2"')
                                                   if oneortwo == '1':
                                                           print('I\'m so sorry, but your attempt to break free has ended up with the man sinking his teeth into your neck and pulling. You are quite dead. Sorry.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           pond = 0
                                                           
                                                   elif oneortwo == 2:
                                                           print('Yes! Your barrel roll sends the man flying off of you and down the road.')
                                                           print('You cannot see him but you hear his footsteps getting more and more distant.')
                                                           print()

                                                   else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           pond = 0

                                                           
                                    else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           pond = 0
                                            
                    else:
                            None    

                    print('Front of the Pond')
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      pond = 0
                      
                      running = 0

                    elif start == 'take boat plug':
                            if 'boat plug' in items:
                                    print('You already have a boat plug.')
                                    print()

                            else:
                                    print('Boat plug taken.')
                                    print()
                                    items.append('boat plug')
                                    boatplug = 0

                    elif start == 'take plug':
                            if 'boat plug' in items:
                                    print('You already have a boat plug.')
                                    print()

                            else:
                                    print('Boat plug taken.')
                                    print()
                                    items.append('boat plug')
                                    boatplug = 0

                    elif start == 'put in boat plug':
                            if boatplug == 1:
                                    print('The boat plug is already in.')
                                    print()

                            else:
                                    print('With great effort you force the plug into place.')
                                    print()
                                    items.remove('boat plug')
                                    boatplug = 1

                    elif start == 'put in plug':
                            if boatplug == 1:
                                    print('The boat plug is already in.')
                                    print()

                            else:
                                    print('With great effort you force the plug into place.')
                                    print()
                                    items.remove('boat plug')
                                    boatplug = 1

                                    

                    elif start == 'look at boat':
                            if 'boat plug' in items:
                                    print('It is a normal-looking John Boat, but the plug seems to be missing.')
                                    print()

                            else:
                                    print('It is a normal-looking John Boat. The plug can be removed.')
                                    print()

                    elif start == 'look in boat':
                            if 'boat plug' in items:
                                    print('It is a normal-looking John Boat, but the plug seems to be missing.')
                                    print()

                            else:
                                    print('It is a normal-looking John Boat. The plug can be removed.')
                                    print()
                            

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'swim':
                            print('You think about it but remember that there\'s a boat right here. Plus, who knows what kind of creatures are lurking in the dark depths.')
                            print()

                    elif start == 'swim across':
                            print('You think about it but remember that there\'s a boat right here. Plus, who knows what kind of creatures are lurking in the dark depths.')
                            print()
                            
                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'east':
                            print('Only way to go that way is in a boat.')
                            print('Would you like to get in the boat and head east?')
                            print()
                            print('yes/no')
                            yesno = input().lower()
                            if yesno == 'yes':
                                    if 'boat plug' in items:
                                            print('You can\'t go across without a boat plug.')
                                            print()
                                    else:
                                            if boatplug == 1:
                                                    
                                            
                                                    print('Alright. You push the boat to the edge, get half-way in, and give a final leg kick to send it smoothly sailing accros the pond, right toward the ominous-looking island.')
                                                    print()
                                                    pond = 0
                                                    place = ['island']

                                            else:
                                                    print('Without a plug, you can\'t get across.')
                                                    print()
                                                    

                            elif yesno == 'no':
                                    print('Mm K. Suit yourself.')
                                    print()

                            else:
                                    print('A "yes" or a "no" are the only answers I\'ll take.')
                                    print()
                                    
                           

                    elif start == 'go east':
                            print('Only way to go that way is in a boat.')
                            print('Would you like to get in the boat and head east?')
                            print()
                            print('yes/no')
                            yesno = input().lower()
                            if yesno == 'yes':
                                    if 'boat plug' in items:
                                            print('You can\'t go across without a boat plug.')
                                            print()
                                    else:
                                            if boatplug == 1:
                                                    
                                            
                                                    print('Alright. You push the boat to the edge, get half-way in, and give a final leg kick to send it smoothly sailing accros the pond, right toward the ominous-looking island.')
                                                    print()
                                                    pond = 0
                                                    place = ['island']

                                            else:
                                                    print('Without a plug, you can\'t get across.')
                                                    print()
                                                    

                            elif yesno == 'no':
                                    print('Mm K. Suit yourself.')
                                    print()

                            else:
                                    print('A "yes" or a "no" are the only answers I\'ll take.')
                                    print()
                            

                    elif start == 'north':
                            print('You can\'t go north from here.')
                            print()
                          
                        

                    elif start == 'go north':
                            print('You can\'t go north from here.')
                            print()
                          
                    elif start == 'south':
                            print('You can\'t go south from here.')
                            print()

                    elif start == 'go south':
                            print('You can\'t go south from here.')
                            print()
                           

                    elif start == 'west':
                            print('You head back to the old shed.')
                            print()
                            pond = 0
                            place = ['inshed']
                            

                    elif start == 'go west':
                            print('You head back to the old shed.')
                            print()
                            pond = 0
                            place = ['inshed']
                            
                    elif start == 'go back':
                            print('You head back to the old shed.')
                            print()
                            pond = 0
                            place = ['inshed']
                    

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                    elif start == 'go to barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    pond = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                    elif start == 'barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    pond = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                      
                      
                    elif start == 'go to shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    pond = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()

                    elif start == 'shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    pond = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()
                     
                      

                    elif start == 'go to house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    pond = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()
                                   
                    elif start == 'house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    pond = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()





                    elif start == 'go to the house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    pond = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()


                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
             
                   

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('Nope. This time you refuse to jump. Who knows what could be lurking around out here.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                     if deadinpond == 0:
                             
                      print(greet['la'])
                      print()
                     else:
                             print('You are in front of the small, hidden pond. There is a rickety old boat next to you and across the pond you can see an island. There is also a man\'s body right here.')
                             print()


                    elif start == 'la':
                      if deadinpond == 0:
                             
                       print(greet['la'])
                       print()
                      else:
                             print('You are in front of the small, hidden pond. There is a rickety old boat next to you and across the pond you can see an island. There is also a man\'s body right here.')
                             print()
                      
                    

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
















##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# place = ['river']-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


        elif place == ['river']:

                

                

 
                
                greet = { 'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in front of a river. There is a landing in front of you with a boat next to it. There is a forest to the east and across the river you see a clearing that you could land at.',
                     'north': 'You walk out from the field to see a small house with a red worn barn to the left of it. There is an overbearing smell of ammonia in the air. In the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making a fool of yourself. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }

                river = 1
                while river == 1:
                    if mightbedead == 1:
                            randomattack == random.randint(1,5)
                            if randomattack == 1:
                                    print('Oh no! The man with the severed arm is back!')
                                    print('press enter')
                                    input()
                                    print('What are you going to do?')
                                    whattodo = input('"run" or "fight"')
                                    if whattodo == 'run':
                                            rand = random.randint(1,2)
                                            if rand == 1:
                                                    print('The man runs after you but slips on something, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('As he falls the man lunges forward and lands directly on his neck.')
                                                    print('press enter')
                                                    input()
                                                    print('There is no need to check again or to double tap. The man is very dead.')
                                                    print()
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinriver = 1
                                            else:
                                                    print('The man runs after you but slips on something, causing him to fall.')
                                                    print('press enter')
                                                    input()
                                                    print('The man falls directly on his face and is stunned.')
                                                    print('press enter')
                                                    input()
                                                    print('You seize the opportunity and quickly jump up and down on his head, flattening him into the ground. The man is very dead now. Good job.')
                                                    print()    
                                                    mightbedead = 0
                                                    dead = 1
                                                    deadinriver = 1

                                    elif whattodo == 'fight':
                                            random = random.randint(1,2)
                                            if random == 1:
                                                    print('You start to think which weapon you are going to use but there is no time; the man lunges forward.')
                                                    print('press enter')
                                                    input()
                                                    print('You dodge and land a punch square on his jaw, causing him to reel backward and fall over.')
                                                    print('press enter')
                                                    input()
                                                    print('HA! What a bit of luck. It seems the man has fallen into the river.')
                                                    print('press enter')
                                                    input()
                                                    print('You watch as he sails on by.')
                                                    print()
                                                    mightbedead = 0
                                                    dead = 1
                                                    
                                            else:
                                                   print('You start to think which weapon you are going to use but there is not time; the man leaps forward.')
                                                   print('press enter')
                                                   input()
                                                   print('You try to dodge but he lands on top of you pinning you down growling and drooling in your face.')
                                                   print('press enter')
                                                   input()
                                                   print('You must decide now! Between two options: option "1" or option "2"')
                                                   oneortwo = input('"1" or "2"')
                                                   if oneortwo == '1':
                                                           print('I\'m so sorry, but your attempt to break free has ended up with the man sinking his teeth into your neck and pulling. You are quite dead. Sorry.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           river = 0
                                                           
                                                   elif oneortwo == 2:
                                                           print('Yes! Your barrel roll sends the man flying off of you and down the river bank.')
                                                           print('You get up and watch him sail down the stream, growling, drooling, and gargaling.')
                                                           print()
                                                           mightbedead = 0
                                                           dead = 1

                                                   else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           river = 0

                                                           
                                    else:
                                                           print('Sorry, but you didn\'t make a valid choice and the man has snapped your neck.')
                                                           print()
                                                           
                                                           place = ['dead']
                                                           river = 0
                                            
                    else:
                            None    

                    print('Front of the River')
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      river = 0
                      
                      running = 0

                    elif start == 'take boat plug':
                            if boatplugriver == 1:
                                    print('You take the boat plug.')
                                    print()
                                    items.append('boat plug')

                            else:
                                    print('There is no boat plug to take.')
                                    print()

                    elif start == 'take plug':
                            if boatplugriver == 1:
                                    print('You take the boat plug.')
                                    print()
                                    items.append('boat plug')

                            else:
                                    print('There is no boat plug to take.')
                                    print()
                                    
                                    

                    elif start == 'look at boat':
                            if boatplugriver == 0:
                                    
                                    print('It is a normal-looking John Boat, but the plug seems to be missing.')
                                    print()

                            else:
                                    print('It is a normal-looking John Boat. The plug can be removed.')
                                    print()

                    elif start == 'look in boat':
                            if boatplugriver == 0:
                                    
                                    print('It is a normal-looking John Boat, but the plug seems to be missing.')
                                    print()

                            else:
                                    print('It is a normal-looking John Boat. The plug can be removed.')
                                    print()

                    elif start == 'put in boat plug':
                            if 'boat plug' in items:
                                    print('You place the plug in the boat.')
                                    print()
                                    boatplugriver = 1
                                    items.remove('boat plug')

                            else:
                                    print('You don\'t have a plug.')
                                    print()

                    elif start == 'put in plug':
                            if 'boat plug' in items:
                                    print('You place the plug in the boat.')
                                    print()
                                    boatplugriver = 1
                                    items.remove('boat plug')

                            else:
                                    print('You don\'t have a plug.')
                                    print()

                    elif start == 'plug in the plug':
                            if 'boat plug' in items:
                                    print('You place the plug in the boat.')
                                    print()
                                    boatplugriver = 1
                                    items.remove('boat plug')

                            else:
                                    print('You don\'t have a plug.')
                                    print()

                    elif start == 'put in the boat plug':
                            if 'boat plug' in items:
                                    print('You place the plug in the boat.')
                                    print()
                                    boatplugriver = 1
                                    items.remove('boat plug')

                            else:
                                    print('You don\'t have a plug.')
                                    print()

                    

                    elif start == 'north':
                            if boatplugriver == 1:
                                    print('You get in the boat and head north up the river to the clearing.')
                                    print()
                                    river = 0
                                    place = ['clearing']

                            else:
                                    print('You can\'t go up the river in the boat unless the boat has a plug.')
                                    print()

                    elif start == 'go north':
                            if boatplugriver == 1:
                                    print('You get in the boat and head north up the river to the clearing.')
                                    print()
                                    river = 0
                                    place = ['clearing']

                            else:
                                    print('You can\'t go up the river in the boat unless the boat has a plug.')
                                    print()

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()
                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    

                    

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()

                    


                    elif start == 'go to barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    river = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                    elif start == 'barn':
                            if mapb == 1:
                                    print('You head to the red, worn barn.')
                                    print()
                                    river = 0
                                    place = ['barn']

                            else:
                                    print('You can\'t see a barn from here.')
                                    print()

                      
                      
                    elif start == 'go to shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    river = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()

                    elif start == 'shed':
                            if mapc == 1:
                                    print('You head to the old shed.')
                                    print()
                                    river = 0
                                    place = ['shed']

                            else:
                                    print('You can\'t see a shed from here.')
                                    print()
                     
                      

                    elif start == 'go to house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    river = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()
                                   
                    elif start == 'house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    river = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()





                    elif start == 'go to the house':
                            if mapb == 1:
                                    print('You head to the house.')
                                    print()
                                    river = 0
                                    place = ['house']

                            else:
                                   print('You can\'t see a house from here. In order to short-cut to a place, you must have visited that place before.')
                                   print()

                    elif start == 'map':

                            print(MAPOFRIVER)
                            print()
             
                      

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('Nope. This time you refuse to jump. Who knows what could be lurking around out here.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                     if deadinriver == 0:
                             
                      print(greet['la'])
                      print()
                     else:
                             print('You are in front of a river. There is a landing in front of you with a boat next to it and also the dead man\'s body. There is a forest to the east and across the river you see a clearing that you could land at.')
                             print()


                    elif start == 'la':
                      if deadinriver == 0:
                             
                       print(greet['la'])
                       print()
                      else:
                             print('You are in front of a river. There is a landing in front of you with a boat next to it and also the dead man\'s body. There is a forest to the east and across the river you see a clearing that you could land at.')
                             print()
                      
                    

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    elif start == 'south':
                            print('You head back to the front of the house.')
                            print()
                            river = 0
                            place = ['fronthouse']

                    elif start == 'go south':
                            print('You head back to the front of the house.')
                            print()
                            river = 0
                            place = ['fronthouse']

                    elif start == 'go back':
                            print('You head back to the front of the house.')
                            print()
                            river = 0
                            place = ['fronthouse']

                    elif start == 'east':
                            print('You cannot go east. It is too thick with trees.')
                            print()

                    elif start == 'go east':
                            print('You cannot go east. It is too thick with trees.')
                            print()

                    elif start == 'west':
                            print('You cannot go west.')
                            print()

                    elif start == 'go west':
                            print('You cannot go west.')
                            print()

                            
                                  

                            
                            

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()






##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################





# place = ['island']----------------------------------------------------------------------------------------------------------------------------------------------------


        elif place == ['island']:

                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are on the island. There is an abundance of trees and thick brush and the only path you see is leading east, straight into the woods. The blood also follows this path.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }

                island = 1
                while island == 1:

                    print('Island')
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      island = 0
                      
                      running = 0

                    elif start == 'take boat plug':
                            if 'boat plug' in items:
                                    print('You already have a boat plug.')
                                    print()

                            else:
                                    print('Boat plug taken.')
                                    print()
                                    items.append('boat plug')
                                    boatplug = 0

                    elif start == 'take plug':
                            if 'boat plug' in items:
                                    print('You already have a boat plug.')
                                    print()

                            else:
                                    print('Boat plug taken.')
                                    print()
                                    items.append('boat plug')
                                    boatplug = 0

                    elif start == 'put in boat plug':
                            if boatplug == 1:
                                    print('The boat plug is already in.')
                                    print()

                            else:
                                    print('With great effort you force the plug into place.')
                                    print()
                                    items.remove('boat plug')
                                    boatplug = 1

                    elif start == 'put in plug':
                            if boatplug == 1:
                                    print('The boat plug is already in.')
                                    print()

                            else:
                                    print('With great effort you force the plug into place.')
                                    print()
                                    items.remove('boat plug')
                                    boatplug = 1

                                    

                    elif start == 'look at boat':
                            if 'boat plug' in items:
                                    print('It is a normal-looking John Boat, but the plug seems to be missing.')
                                    print()

                            else:
                                    print('It is a normal-looking John Boat. The plug can be removed.')
                                    print()

                    elif start == 'look in boat':
                            if 'boat plug' in items:
                                    print('It is a normal-looking John Boat, but the plug seems to be missing.')
                                    print()

                            else:
                                    print('It is a normal-looking John Boat. The plug can be removed.')
                                    print()
                            

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                    elif start == 'swim':
                            print('You think about it but remember that there\'s a boat right here. Plus, who knows what kind of creatures are lurking in the dark depths.')
                            print()

                    elif start == 'swim across':
                            print('You think about it but remember that there\'s a boat right here. Plus, who knows what kind of creatures are lurking in the dark depths.')
                            print()
                            
                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'north':
                            print('you can\'t go north from here.')
                            print()

                    elif start == 'go north':
                            print('you can\'t go north from here.')
                            print()
                            

                    elif start == 'east':
                            print('You head east into the deep woods following the trail of blood.')
                            print()
                            island = 0
                            place = ['islandwoods']
                            
                          
                        

                    elif start == 'go east':
                            print('You head east into the deep woods following the trail of blood.')
                            print()
                            island = 0
                            place = ['islandwoods']
                          
                    elif start == 'south':
                            print('You can\'t go south from here.')
                            print()

                    elif start == 'go south':
                            print('You can\'t go south from here.')
                            print()
                           

                    elif start == 'west':
                            if boatplug == 1:
                                    print('You head back across the pond.')
                                    print()
                                    island = 0
                                    place = ['pond']

                            else:
                                    print('You aren\'t going anywhere without a plug in that boat!')
                                    print()
                            

                    elif start == 'go west':
                             if boatplug == 1:
                                    print('You head back across the pond.')
                                    print()
                                    island = 0
                                    place = ['pond']

                             else:
                                    print('You aren\'t going anywhere without a plug in that boat!')
                                    print()
                            
                    elif start == 'go back':
                             if boatplug == 1:
                                    print('You head back across the pond.')
                                    print()
                                    island = 0
                                    place = ['pond']

                             else:
                                    print('You aren\'t going anywhere without a plug in that boat!')
                                    print()
                    

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                    

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
             
                   

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('Nope. This time you refuse to jump. Who knows what could be lurking around out here.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   
                      
                    elif start == 'look around':
                      print(greet['la'])
                      print()

                    elif start == 'la':
                      print(greet['la'])
                      print()
                      
                    

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()

                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()








##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################




# place = ['islandwoods']

        elif place == ['islandwoods']:
                
                

                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are in a circular clearing on the island. It looks at though it was a camping spot because there is a fire circle with a picnick table next to it.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }

                islandwoods = 1
                while islandwoods == 1:

                    print('Camping Spot')
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      islandwoods = 0
                      
                      running = 0

                    
                            

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                                

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                  
                            
                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()
                                            
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()
                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    
                    

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                    

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
             
                   

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('Nope. This time you refuse to jump. Who knows what could be lurking around out here.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()   


                    
                      
                    elif start == 'look around':
                            if dead == 1:
                                           print('You see a fire spot, a picnick table, and the dead man\'s body on the ground.')
                                           print()

                                
                            elif mightbedead == 1:
                                           
                                           if couldbedead == 1:
                                                   print('You see a fire spot, a picnick table, and the dead man\'s body on the ground.')
                                                   print()

                                           else:
                                                   print('You see the fire spot and the table but you don\'t see the man anywhere. You see footprint\'s leading away into the woods. This is not good.')
                                                   print()

                            elif notdead == 1:
                                    print('You see the fire spot and the table but you don\'t see the man anywhere. You see footprint\'s leading away into the woods. This is not good.')
                                    print()
                                    
                            else:                
                                    print('You shine your light around and see that you are in a circular clearing on the island. It appears to be a camping site because you see a fire pit and... What THE! You see a man lying on a picnick table bleeding! His arm is missing and he\'s not moving!')
                                    print()
                                    print('PRESS ENTER')
                                    input()
                                    
                            
                                    
                                    
                                    print('You run to the man to check on him. You feel a pulse and try to rouse him awake.')
                                    print('press enter to rouse:')
                                    input()
                                    print()
                                    print('He awakes groggily.')
                                    print('...')
                                    time.sleep(1)
                                    print('...')
                                    time.sleep(1)
                                    print('MAN: "hmm..."')
                                    time.sleep(.5)
                                    
                                    print('MAN: "mmm...Wh-Where am I?')

                                    
                                    whoareyou = input('Response...')

                                    
                                    if whoareyou == 'you\'re on an island':
                                            print('MAN: "Who are you?"')
                                            print()
                                            whodat = input('Response...')
                                            if whodat == 'i don\'t know':
                                                    print('IT HURTS! MAKE IT STOP!!! PLEASSSEE!!')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('PRESS ENTER')
                                                    input()
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             choice = input('"run" or "finish"')
                                                                             print()
                                                                             dude = 1
                                                                             while dude == 1:
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" and "finish"')
                                                                                      print()
                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']
                                            else:
                                                    print('MAN: "Huh? What!? What\'s happening!? Please make it stop! It burns! My arm, it burns!"')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('PRESS ENTER')
                                                    input()
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             choice = input('"run" or "finish"')
                                                                             print()
                                                                             dude = 1
                                                                             while dude == 1:
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" or "finish"')
                                                                                      print()
                                                                             
                                                                             

                                                                            
                                                                                            

                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']               
                                            

                                    elif whoareyou == 'an island':
                                            print('MAN: "What happened?"')
                                            time.sleep(.5)
                                            print('MAN: "ughh..."')
                                            time.sleep(1)
                                            print('The man sits up.')
                                            whodat = input('Response...')
                                            if whodat == 'you\'re bleeding':
                                                    print('MAN: "Help me... Please help me....')
                                                    print('IT HURTS! MAKE IT STOP!!! PLEASSSEE!!')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('press enter:')
                                                    input()
                                                    
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             
                                                                             dude = 1
                                                                             while dude == 1:
                                                                              choice = input('"run" or "finish"')
                                                                              print()       
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" and "finish"')
                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']                

                                    else:
                                                    print('MAN: ".... don\'t...feel...good....."')
                                                    time.sleep(.5)
                                                    print('MAN: "...arm....hurts"')
                                                    time.sleep(.5)
                                                    print('MAN: "Who are you?"')
                                                    print('IT HURTS! MAKE IT STOP!!! PLEASSSEE!!')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('press enter')
                                                    input()
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             choice = input('"run" or "finish"')
                                                                             print()
                                                                             dude = 1
                                                                             while dude == 1:
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" and "finish"')
                                                                                      print()
                     
                            
                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']      

                              
                    elif start == 'la':
                                   if dead == 1:
                                           print('You see a fire spot, a picnick table, and the dead man\'s body on the ground.')
                                           print()

                                
                                   elif mightbedead == 1:
                                           
                                           if couldbedead == 1:
                                                   print('You see a fire spot, a picnick table, and the dead man\'s body on the ground.')
                                                   print()

                                           else:
                                                   print('You see the fire spot and the table but you don\'t see the man anywhere. You see footprint\'s leading away into the woods. This is not good.')
                                                   print()
                                   elif notdead == 1:
                                           print('You see the fire spot and the table but you don\'t see the man anywhere. You see footprint\'s leading away into the woods. This is not good.')
                                           print()
                                   else:                
                                    print('You shine your light around and see that you are in a circular clearing on the island. It appears to be a camping site because you see a fire pit and... What THE! You see a man lying on a picnick table bleeding! His arm is missing and he\'s not moving!')
                                    print()
                                    
                            
                                    
                                    
                                    print('You run to the man to check on him. You feel a pulse and try to rouse him awake.')

                                    print('press enter to rouse:')
                                    input()
                                    print('He awakes groggily.')
                                    print('...')
                                    time.sleep(1)
                                    print('...')
                                    time.sleep(1)
                                    print('MAN: "hmm..."')
                                    time.sleep(.5)
                                    
                                    print('MAN: "mmm...Wh-Where am I?')

                                    
                                    whoareyou = input('Response...')

                                    
                                    if whoareyou == 'you\'re on an island':
                                            print('MAN: "Who are you?"')
                                            print()
                                            whodat = input('Response...')
                                            if whodat == 'i don\'t know':
                                                    print('IT HURTS! MAKE IT STOP!!! PLEASSSEE!!')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('press enter')
                                                    input()
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             choice = input('"run" or "finish"')
                                                                             print()
                                                                             dude = 1
                                                                             while dude == 1:
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" and "finish"')
                                                                                      print()
                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']      
                                            else:
                                                    print('MAN: "Huh? What!? What\'s happening!? Please make it stop! It burns! My arm, it burns!"')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('press enter')
                                                    input()
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             choice = input('"run" or "finish"')
                                                                             print()
                                                                             dude = 1
                                                                             while dude == 1:
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" or "finish"')
                                                                                      print()
                                                                             
                                                                             

                                                                            
                                                                                            

                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']  
                                            

                                    elif whoareyou == 'an island':
                                            print('MAN: "What happened?"')
                                            time.sleep(.5)
                                            print('MAN: "ughh..."')
                                            time.sleep(1)
                                            print('The man sits up.')
                                            whodat = input('Response...')
                                            if whodat == 'you\'re bleeding':
                                                    print('MAN: "Help me... Please help me....')
                                                    print('IT HURTS! MAKE IT STOP!!! PLEASSSEE!!')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('press enter')
                                                    input()
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             
                                                                             dude = 1
                                                                             while dude == 1:
                                                                              choice = input('"run" or "finish"')
                                                                              print()       
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" and "finish"')
                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']                                    

                                    else:
                                                    print('MAN: ".... don\'t...feel...good....."')
                                                    time.sleep(.5)
                                                    print('MAN: "...arm....hurts"')
                                                    time.sleep(.5)
                                                    print('MAN: "Who are you?"')
                                                    print('IT HURTS! MAKE IT STOP!!! PLEASSSEE!!')
                                                    print()
                                                    print('The man collapses on the table, dropping something. You try to awaken him again but you can\'t. You sit there for what seems like forever, shaking heavily.')
                                                    print('You then check to see what he dropped and see that it is a photo of a young man, who looks a lot like the one beside you, and a young women embracing each other, obviously in love. You check the back of it. It says, "Danny and Trish, Sepetember 2008".')
                                                    print('You sit there even longer contemplating what just happened when suddenly you sense somthing moving next to you.')
                                                    print('It\'s the man trying to get up! You try and help him sit up. He is muttering indistinctly to himself.')
                                                    print('press enter')
                                                    input()
                                                    time.sleep(1)
                                                    print('MAN: "..."')
                                                    time.sleep(.5)
                                                    print('MAN: "...mmhh...."')
                                                    print('All of a sudden the man attacks, having strength no regular man in his condition should have.')
                                                    print('He lunges at you but misses and hits the ground!')
                                                    print('You shout and plead to him but he seems not to listen. He is now starting to growl and moan. You see drool dripping from his mouth.')
                                                    print('What are you going to do?')
                                                    
                                                    whatwillyoudo = input('"run" or "fight"...')
                                                    if whatwillyoudo == 'fight':
                                                            print('With what will you fight him?')
                                                            print('Something from your items? or perhaps your hands? Choose quickly!')
                                                            print()
                                                            this = 1
                                                            while this == 1:
                                                                    
                                                             item = input('Fight with what...')
                                                             if item == 'flashlight':
                                                                    if 'flashlight' in items:
                                                                            outcome = random.randint(1,2)
                                                                            if outcome == 1:
                                                                                    print('He lunges again and you land a blow to his head making him reel and sway drousily.')
                                                                                    print('You hit him again and he falls to the ground, twitching... he might be dead.')
                                                                                    print('"walk away" or "double tap"?')
                                                                                    which = input('"walk away or "double tap"')
                                                                                    if which == 'walk away':
                                                                                            print('You leave the man and go back to the island.')
                                                                                            print()
                                                                                            islandwoods = 0
                                                                                            place = ['island']
                                                                                            mightbedead = 1
                                                                                            this = 0

                                                                                    elif which == 'double tap':
                                                                                            print('You bash the man again in the head. He makes a final twitch and goes still. He is dead.')
                                                                                            print()
                                                                                            dead = 1
                                                                                            this = 0

                                                                                    else:
                                                                                            print('Your indecision, or lack of ability to follow directions, has caused you to miss that the man has gotten up and has bitten you on the neck.')
                                                                                            print('You try to get away but he throws you to the ground and begins to bite and tear. You die a most horrible death.')
                                                                                            islandwoods = 0
                                                                                            place = ['dead']
                                                                                            this = 0
                                                                                            running = 0

                                                                            else:
                                                                                    print('You don\'t have that.')
                                                                                    print('Uh-oh, your fumbiling mistake has caused the man to jump on you and begin to try and bite you. You throw him off and you get back up. Now what?')
                                                                                    
                                                                                                            

                                                             elif item == 'machete':
                                                                    if 'machete' in items:
                                                                            print('You take a whack at the man and nearly cut his head off.')
                                                                            print('You hit him again to make sure.')
                                                                            print('Yep. The man, although grudgingly, has parted ways with his head. He is clearly dead.')
                                                                            this = 0
                                                                            dead = 1
                                                                            print()

                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'corn':
                                                                     if 'corn' in items:
                                                                             print('Really?! OK then.')
                                                                             corn = random.randint(1,2)
                                                                             if corn == 1:
                                                                                     print('Amazingly, you manage to jam the corn in the man\'s and he falls down dead. Unbelievable.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0

                                                                             else:
                                                                                     print('You dumbassness has lead to your unpreventable death. The last thing you see before this crazed man kills you is the weapon of corn falling to the ground. Good job')
                                                                                     print()
                                                                                     this = 0
                                                                                     running = 0
                                                                                     place = ['dead']

                                                             elif item == 'arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')

                                                             elif item == 'severed arm':
                                                                    if 'severed arm' in items:
                                                                            
                                                                     print('You wail away at the man with his own severed arm.')
                                                                     print('You astonishingly manage to beat him the the ground. You keep beating until you know he\'s dead. He is definitely dead.')
                                                                     dead = 1
                                                                     this = 0
                                                                     
                                                                    else:
                                                                            print('You don\'t have that.')
                                                                            print('Great! Now the man lunges again because of your forgetfulness but thankfully misses again. Now what?')
                                                                            
                                                             elif item == 'hands':
                                                                     hands = random.randint(1,2)
                                                                     if hands == 1:
                                                                             print('You grab the man and begin to beat him, dodging the mans attacks. You wrestle him to the ground and continue to beat him. You begin to kick wildly at the mans gut and head. He has stopped moving. He is dead.')
                                                                             print()
                                                                             dead = 1
                                                                             this = 0

                                                                     else:
                                                                             print('You try to hit the man but miss. He hits you with a flailing arm and you hit the ground.')
                                                                             print('He jumps on top of you and you begin to wrestle.')
                                                                             print('...')
                                                                             time.sleep(.5)
                                                                             print('...ugh....')
                                                                             time.sleep(1)
                                                                             print('.....ahhh..')
                                                                             print('...')
                                                                             print('Miraculously you have managed to knock him out cold, but he could be dead. What will you do?')
                                                                             choice = input('"run" or "finish"')
                                                                             print()
                                                                             dude = 1
                                                                             while dude == 1:
                                                                                     
                                                                              if choice == 'run':
                                                                                     print('You quickly leave the body and head back to the shore of the island.')
                                                                                     print()
                                                                                     this = 0
                                                                                     islandwoods = 0
                                                                                     place = ['islandwoods']
                                                                                     mightbedead = 1
                                                                                     dude = 0

                                                                              elif choice == 'finish':
                                                                                     print('You take your foot and crush in his skull. He is definitely dead.')
                                                                                     print()
                                                                                     dead = 1
                                                                                     this = 0
                                                                                     dude = 0

                                                                              else:
                                                                                      print('You must pick between "run" and "finish"')
                                                                                      print()
                                            

                                                    elif whatwillyoudo == 'run':
                                                            that = 1
                                                            
                                                            
                                                            while that == 1:
                                                                    
                                                             if randomrun == 1:
                                                                    
                                                                    print('You turn around to run and the man follows but he ends up tripping and impaling himself with an old tent stake.')
                                                                    print('The man is quite clearly dead. But you decide to dip out anyway and head back to the shore of the island.')
                                                                    dead = 1
                                                                    that = 0
                                                                    islandwoods = 0
                                                                    place = ['islandwoods']

                                                             elif randomrun == 2:
                                                                     print('You turn to run back to the island but the man grabs you. He throws you to the ground with a murderous look in his eye. He is about to finish you off when you hear a sound coming from the woods. Miraculously the man leaves you alone to go chase the sound.')
                                                                     print()
                                                                     that = 0
                                                                     notdead = 1

                                                             else:
                                                                   print('You turn to go back to the shore of the island but the man grabs you. You struggle but he holds firm. Try as you might to free yourself the crazed man holds you tight and begins to bite and pull at you. I won\'t say anymore except that you\'re dead. Sorry.')
                                                                   print()
                                                                   that = 0
                                                                   this = 0
                                                                   running = 0
                                                                   place = ['dead']

                                                    else:
                                                            print('Your lack of spelling has cost you your life. Good job buddy.')
                                                            print()
                                                            that = 0
                                                            this = 0
                                                            running = 0
                                                            place = ['dead']      







                                           
                      
                    

                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()
                      
                    elif start == 'go back':
                            print('You head back to the shore of the island.')
                            print()
                            islandwoods = 0
                            place = ['island']

                    elif start == 'go west':
                            print('You head back to the shore of the island.')
                            print()
                            islandwoods = 0
                            place = ['island']

                    elif start == 'west':
                            print('You head back to the shore of the island.')
                            print()
                            islandwoods = 0
                            place = ['island']

                    elif start == 'go east':
                            print('You can\'t go east from here.')
                            print()

                    elif start == 'east':
                            print('You can\'t go east from here.')
                            print()

                    elif start == 'go north':
                            print('You can\'t go north from here.')
                            print()

                    elif start == 'north':
                            print('You can\'t go north from here.')
                            print()

                    elif start == 'go south':
                            print('You can\'t go south from here.')
                            print()

                    elif start == 'south':
                            print('You can\'t go south from here.')
                            print()

                    
                            
                            
                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
        
        elif place == ['clearing']:
                print('Yes! You have made it to the clearing across the river.')
                print('press enter:')
                input()
                print('You pull the boat up out of the water and walk forward.')
                print('press enter:')
                input()
                print('The sun is coming up so you turn off your flashlight and sit on a stump reflecting what a night you just had.')
                print('press enter:')
                input()
                print('But this is no time to rest and you get up off the stump.')
                print('press enter:')
                input()
                print('You must continue.')
                print('press enter:')
                input()
                print('But as you go to walk forward, something hits you. Your muscles have gone rigid and you can\'t move. You feel yourself burning all over.')
                print('press enter:')
                input()
                print('...')
                time.sleep(1)
                print('...')
                time.sleep(.5)
                print('You try to wake up.')
                print('press enter to try to wake up:')
                input()
                print('You try as hard as you can but to no use.')
                print('press enter:')
                input()
                print('The last thing you hear before you black out is...')
                print('press enter:')
                input()
                print('MAN: "This one doesn\'t look to be inf....ed. Quick, get h.. to the house We nee. to get h.. to saf... and ...... these wo....')
                print()
                print()
                
                print('Congratulations. You have finished Pyork. Well done. But do not get too comfortable.')
                print('press enter:')
                input()
                print('This is only the beginning.......')
                
                print()
                running = 0
                place = ['YOU WON']




#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################      
#########################################################################################################################################################################
# place = ['truck']

        elif place == ['truck']:
                greet = {'ihy' : 'Well I\'m not too fond of you either.',
                     'ily' : 'Whoa now! That\'s a little strong.',
                     'la'  : 'You are inside the truck. It is an old white Ford F-150. It is surprisingly clean and organized, not counting the dust mind you, but it is just regular truck; complete with glovebox and everything.',
                     'north': 'You walk out from the field to see a small house with a red worn-down barn to the left of it. There is an overbearing smell of ammonia in the air and in the distance you hear what sounds like howling. Perhaps it\'s just the wind.',
                     'hey'  : 'What\'s up?',
                     'south': 'You can\'t go south.',
                     'west' : 'You can\'t go west.',
                     'music': 'This is Mozart\'s Requiem Mass in D Minor.',
                     'cuss' : 'Ha Ha! Getting frustrated?',
                     'field': 'It is a corn field but the section you are in appears to\nhave been trampled over and broken.',
                     'dude' : 'Sweet!',
                     'whatup' : 'Nothing much, how about yourself?',
                     'heyt'   : 'Hey there.',
                     'hello'  : 'Hello.',
                     'crank'  : 'crank that soulja boy!',
                     'sweet'  : 'Dude!',
                     'fu'     : 'Fuck you too!',
                     'ho'     : 'Ho.',
                     'idly'   : 'Whateva.',
                     'jump'   : 'You jump up and down making the bent-over corn crack. You begin to breath\nheavily',
                     'smile'  : 'There\'s not much to smile about but you go ahead anyway.',
                     'grin'   : 'You grin large and proud. A little more and you\'ll shame the moon.',
                     'dance'  : 'You begin to boogy down. Hopefully no one saw you.',
                     'yb'     : 'tee hee',
                     'sing'   : 'You can\'t sing now. You don\'t know who could be watching.',
                     'fag'    : 'See a mirror or something?',
                     'spell'  : 'Ha! Way to misspell while trying to insult me!',
                     'mmm'    : 'Mm Hmm',
                     'pg'     : 'Pretty good. How \'bout yourself?',
                     'ys'     : 'Yo Momma!',
                     'take'   : 'What do you want to take?'

                         }

                truck = 1
                while truck == 1:

                    print('Truck')
                    start = input('You: ').lower()
                    print()
                    
                    if start == 'quit':
                      print('Bye Bye')
                      place = ['20']
                      truck = 0
                      
                      running = 0

                   
                            

                    elif start == 'read letter':
                            if 'letter' in items:
                                    print(letter)
                                    print()

                            else:
                                    print('You don\'t have a letter.')
                                    print()

                    elif start == 'i love katie':
                            print('The very mostest babe!')
                            print()

                            
                    elif start == 'i love jp':
                            print('Who doesn\'t?')
                            print()

                    elif start == 'examine':
                            print('What do you want to examine?')
                            print()
                            ex = input('...').lower()
                            if ex == 'corn':
                                    if 'corn' in items:
                                            print('It is just a regular ear of corn except for a few "buggy" pieces here and there. Nothing out of the ordinary.')
                                            print()

                                    else:
                                            print('You don\'t have any corn to examine.')
                                            print()

                            elif ex == 'boat plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()

                            elif ex == 'plug':
                                    if 'boat plug' in items:
                                            print('It is a regular boat plug that can be found in, and used, in any small boat.')
                                            print()

                                    else:
                                            print('You don\'t have a boat plug.')
                                            print()
                            elif ex == 'note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'letter':
                                    if 'letter' in items:
                                            
                                            print('It is the letter from the kitchen. It seems very well-written and looks almost new.')
                                            print()

                                    else:
                                            print('You don\'t have a letter.')
                                            print()

                            elif ex == 'truck keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'severed arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()
                                            
                            elif ex == 'keys':
                                    if 'truck keys' in items:
                                            print('There is only one key, a vehicle key, but two rings. It\'s as if another key was here but was taken.')
                                            print()

                                    else:
                                            print('You don\'t have any keys to examine.')
                                            print()

                            elif ex == 'barn note':
                                    if 'barn note' in items:
                                            
                                            print('It is the note you found in the loft of the barn. The paper looks old and worn but still legible.')
                                            print()

                                    else:
                                            print('You don\'t have a note to examine.')
                                            print()

                            elif ex == 'arm':
                                    if 'severed arm' in items:
                                            print('It is the severed arm you found and, for some strange reason, decided to keep. You look close and see that the arm appears to have been bitten down to the bone and then was ripped from the body.')
                                            print()

                                    else:
                                            print('You do not have one of those.')
                                            print()

                            elif ex == 'flashlight':
                                    if 'flashlight' in items:
                                            print('It is a regular metal flashlight. Feels very heavy and quite well made. It glows with a bright intensity and illuminates to quite a distance.')
                                            print()

                                    else:
                                            print('You don\'t have a flashlight.')
                                            print()

                            elif ex == 'machete':
                                    if 'machete' in items:
                                            print('It is a normal-looking machete. It is rather sharp and looks very new, despite a few scratches here and there. It would make an excellent weapon.')
                                            print()

                                    else:
                                            print('You don\'t have a machete.')
                                            print()
                                            

                            else:
                                    print('Can\'t help you there. Perhaps if you typed it in another way. Then I could help you.')
                                    print()

                    elif start == 'north':
                            print('You can\'t go north from here.')
                            print()

                    elif start == 'go north':
                            print('You can\'t go north from here.')
                            print()
                            

                    elif start == 'east':
                            
                         print('You get out the truck on the passenger side.')
                         print()
                         truck = 0
                         place = ['fronthouse']
                          
                        

                    elif start == 'go east':
                         print('You get out the truck on the passenger side.')
                         print()
                         truck = 0
                         place = ['fronthouse']
                          
                    elif start == 'south':
                            print('You can\'t go south from here.')
                            print()

                    elif start == 'go south':
                            print('You can\'t go south from here.')
                            print()
                           

                    elif start == 'west':
                         print('You get out the truck on the driver side.')
                         print()
                         truck = 0
                         place = ['fronthouse']
                            

                    elif start == 'go west':
                         print('You get out the truck on the driver side.')
                         print()
                         truck = 0
                         place = ['fronthouse']
                            
                    elif start == 'go back':
                         print('You get out the truck.')
                         print()
                         truck = 0
                         place = ['fronthouse']
                         
                    elif start == 'get out':
                         print('You get out the truck.')
                         print()
                         truck = 0
                         place = ['fronthouse']

                    elif start == 'read barn note':
                            if 'barn note' in items:
                                    print(barnnote)
                                    print()
                            else:
                                    print('You don\'t have that yet.')
                                    print()


                    

                    elif start == 'map':

                            if mapa == 1:
                                    if mapb == 1:
                                            if mapc == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
                                            elif mapfront == 1:
                                                    if mapc == 1:
                                                            print(MAPFRONTOFHOUSE)
                                                            print()
                                                            
                                                    else:
                                                            
                                                            print(MAPFRONTOFHOUSENOEAST)
                                                            print()

                                            


                                            else:
                                                    
                                                    print(MAPB)
                                                    print()
                                    elif mapc == 1:
                                            if mapb == 1:
                                                    if mapofpond == 1:
                                                            if mapfront == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()

                                                            else:
                                                                    print(MAPOFPONDNOTRUCK)
                                                                    print()

                                                    elif mapfront == 1:
                                                            if mapofpond == 1:
                                                                    print(MAPOFPONDTRUCK)
                                                                    print()
                                                            else:
                                                                    print(MAPFRONTOFHOUSE)
                                                                    print()
                                                                    

                                                    else:
                                                            
                                                        
                                                            print(MAPD)
                                                            print()
        

                                            elif mapfront == 1:
                                                    if mapofpond == 1:
                                                            print(MAPOFPONDTRUCK)
                                                            print()

                                                    else:
                                                            print(MAPFRONTOFHOUSENOBARN)


                                            elif rightofhouse == 1:
                                                    print(YRMAP1)
                                                    print()
                                            else:
                                                    
                                                    print(MAPC)
                                                    print()

                                 

                                    
                                    else:
                                            print(MAPA)
                                            print()
                                    
             
                   

                    elif start == 'i hate you':
                      print(greet['ihy'])
                      print()

                    elif start == 'check items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    elif start == 'items':
                      if items == []:
                         print('You don\'t have any at the moment')
                         print()
                      else:
                         print(items)
                         print()

                    

                    elif start == 'eat corn':
                      if 'corn' in items:
                         print('You take the ear and gobble it down. Delicious')
                         items.remove('corn')
                         print()
                      else:
                         print('You don\'t have any corn in your items')
                         print()

                    elif start == 'throw corn':
                      if 'corn' in items:
                         where = input('Where do you want to throw the corn? ').lower()
                         
                         if where == 'me':
                            items.remove('corn')
                            print('OW! Why would you do that to yourself?!')
                            print()
                            
                         elif where == 'there':
                            print('You throw the corn over there.')
                            print()
                            items.remove('corn')
                            
                         elif where == 'bird':
                            print('You can\'t see any bird around.')
                            print()

                         elif where == 'you':
                            print('Yeah, you wish you could hit this!')
                            print()

                         else:
                            print('You can\'t do that.')
                            print()

                      else:
                         print('You don\'t have any corn to throw')
                         print()
                     

                      

                    elif start == 'fag':
                      print(greet['fag'])
                      print()

                    elif start == 'faggot':
                      print(greet['fag'])
                      print()

                    elif start == 'you suck':
                      print(greet['ys'])
                      print()

                    elif start == 'whatever':
                      print(greet['mmm'])
                      print()

                    elif start == 'how are you':
                      print(greet['pg'])
                      print()

                    elif start == 'fagget':
                      print(greet['spell'])
                      print()

                    elif start == 'fagg':
                      print(greet['spell'])
                      print()

                    elif start == 'jump':
                      print('Nope. This time you refuse to jump. Who knows what could be lurking around out here.')
                      print()

                    elif start == 'dance':
                      print(greet['dance'])
                      print()

                    elif start == 'sing':
                      print(greet['sing'])
                      print()

                    elif start == 'fuck you':
                      print(greet['fu'])
                      print()

                    elif start == 'smile':
                      print(greet['smile'])
                      print()

                    elif start == 'grin':
                      print(greet['grin'])
                      print()

                    elif start == 'bitch':
                      print(greet['ho'])
                      print()

                    elif start == 'i don\'t like you':
                      print(greet['idly'])
                      print()

                    elif start == 'i love you':
                      print(greet['ily'])
                      print()

                    elif start == 'hey':
                      print(greet['hey'])
                      print()

                    elif start == 'hi':
                      print(greet['heyt'])
                      print()

                    elif start == 'hello':
                      print(greet['hello'])
                      print()

                    elif start == 'dude':
                      print(greet['dude'])
                      print()

                    elif start == 'sweet':
                      print(greet['sweet'])
                      print()   

                    elif start == 'you':
                      print(greet['crank'])
                      print()
                    elif start == 'crank engine':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It looks at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()  
                    elif start == 'crank truck':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It look at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()  
                    elif start == 'crank':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It look at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()
                    elif start == 'turn on truck':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It look at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()  
                    elif start == 'turn on':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It look at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()    
                    elif start == 'start engine':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It look at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()  
                    elif start == 'start truck':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It look at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()
                    elif start == 'start':
                           if turnedover == 0: 
                           
                            print('You try to turn the key and... amazingly it works the truck has started and you shine your lights on the road ahead of you. You may just make it out alive; but wait! What is that in front of you?! It\'s some kind of creature that is almost dog like. It\'s coming right for you!.')
                            print('press enter:')
                            input()
                            print('It leaps forward towards you and lands on the hood of the truck, crushing it. The truck shuts off. It look at you intensly and suddenly lunges an arm through the window, but it backfires; it is now stuck in the glass.')
                            print('press enter:')
                            input()
                            print('With the creature thrashing so forociously, it has dislodged the glove box revealing a pistol.')
                            print('You take the pistol and shoot at the creature, aiming for its head.')
                            print('press enter:')
                            input()
                            print('It shrieks with agony and sways back and forth on the truck. All of a sudden it grabs the pistol and jurks its arm back through the glass.')
                            print('press enter:')
                            input()
                            print('Badly hurt, the creature runs off down the road and into the woods carrying the pistol with it.')
                            brokeglass = 1
                            turnedover = 1
                           else:
                                   print('The truck will not start again.')
                                   print()
                           
                                   
                            
                    elif start == 'look around':
                     if brokeglass == 0:       
                      print(greet['la'])
                      print()
                     else:
                             print('You are in the truck. There is glass everywhere from where the creature punched through the windshield.')
                             print()

                    elif start == 'la':
                      if brokeglass == 0:       
                       print(greet['la'])
                       print()
                      else:
                             print('You are in the truck. There is glass everywhere from where the creature punched through the windshield.')
                             print()
                      
                    

                    elif start == 'drive':
                            if turnedover == 0:
                                    print('You\'ll have to crank the truck up first.')
                                    print()

                            else:
                                    print('The truck will not start again.')
                                    print()

                    elif start == 'drive east':
                            if turnedover == 0:
                                    print('You\'ll have to crank the truck up first.')
                                    print()

                            else:
                                    print('The truck will not start again.')
                                    print()

                    elif start == 'drive truck':
                            if turnedover == 0:
                                    print('You\'ll have to crank the truck up first.')
                                    print()

                            else:
                                    print('The truck will not start again.')
                                    print()
                                    

                    elif start == 'damn':
                      print(greet['cuss'])
                      print()

                    elif start == 'you bastard':
                      print(greet['yb'])
                      print()

                    elif start == 'fuck':
                      print(greet['cuss'])
                      print()

                    elif start == 'shit':
                      print(greet['cuss'])
                      print()
                    elif start == 'open':
                            if turnedover == 0:
                            
                                    print('The glovebox is locked and cannot be opened.')
                                    print()

                            else:
                                    print('The glovebox is already open and there is nothing in it.')
                                    print()
                            
                    elif start == 'open glovebox':
                            if turnedover == 0:
                            
                                    print('The glovebox is locked and cannot be opened.')
                                    print()

                            else:
                                    print('The glovebox is already open and there is nothing in it.')
                                    print()

                    elif start == 'glovebox':
                            if turnedover == 0:
                            
                                    print('The glovebox is locked and cannot be opened.')
                                    print()

                            else:
                                    print('The glovebox is already open and there is nothing in it.')
                                    print()       
                    

                    elif start == 'what\'s up':
                      print(greet['whatup'])
                      print()

                    else:
                        print('I don\'t know the word(s): ' + start )
                        print()
                        
        

couldbedead = random.randint(1,2)
mapb = 0
mapc = 0
running = 1
place = ['field']
door = 0
arm = 0
eastopen = 0
memory1 = 0
lrmap = 0
mapfront = 0
exarm = 0
inshedmemory = 0
playedpiano = 0
mapofpond = 0
rightofhouse = 0
toolchoice = 0
moves = 0
lookedattable = 0
ovenopened = 0
microwaveopened = 0
fridgeopened = 0
boatplug = 1
boatplugriver = 0
foundman = 0
checkonman = 0
dead = 0
notdead = 0                                                                          
mightbedead = 0   
bathroommap = 0
bedroommap = 0
studymap = 0
whichroomhaskey = random.randint(1,3)
shower = 0
brokeglass = 0
turnedover = 0
randomrun = random.randint(1,3)
deadinfield = 0
deadinfronthouse = 0
deadinpond = 0
deadinriver = 0
PYDOC = '''

                             'Pyork'
                               by
                         Joshua Powell


Hello and welcome to Pyork! It is a text-based adventure game modeled
after the "Zork" games (actually just the first Zork, thank you
"Black Ops") and made with python and pygame, hence the name
'Py' - 'ork'. It is basically a "puzzle" game (or whatever the word is).        You basically need to find "part 1" to get through "door 2" and etc.

	
GUIDELINES

-There are a few things to know about Pyork before beginning, just to
help you along. Your "responses", that is what you type onto the screen        , are not case-sensitive and you do not need punctuation.
	
-Also, I have tried to make every response, that is obvious, able to by
typed  but usually your "responses" don't really need an article
(I tried to make everything short-hand). ie: "swing sword" not "swing
the sword" and "take nap" not "take a nap".
        
-There are a few special functions written into Pyork that may be useful
to you. There is the "map" function (which is memory-mapped), the
"items" function (to check your inventory), the "examine" function
(which is used to more closely examine the items in your "items"),
and the "la" (look around) function (which lets you check out the area
that you are in).
        
-Most of the direction responses are strictly "north, east, south,
west". There are no rights or lefts although you can sometimes
substitute "south" for the response "go back".

-Use the word "take" whenever you want to pick up things.

-Your first attempt at "doing" something might not work because it
is worded slightly different. Try different words or phrases,
possibly even different spellings.
        
'''

letter = '''
        Dear John,
I really enjoyed lunch with you the other day. We should definitely
do it again. Just call me when you get a chance.

Love, Sandy

p.s. I didn\'t know what to think when we headed in that shed. I never would have guessed that door was there.

'''








while running == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    main()
   

    
    



    



