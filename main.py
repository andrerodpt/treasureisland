print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
dino_ascii_art = '''
                           _
                        __~a~_
                        ~~;  ~_
          _                ~  ~_                _
         '_\;__._._._._._._]   ~_._._._._._.__;/_`
         '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
         (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
        (/ / / / / | | | ~(/    \) ~ | | \ \ \ \ \)
       (/ / / / /  ~ ~ ~   (/  \)    ~ ~  \ \ \ \ \)
      (/ / / / ~          / (||)|          ~ \ \ \ \)
      ~ / / ~            M  /||\M             ~ \ \ ~
       ~ ~                  /||\                 ~ ~
                           //||\\
                           //||\\
                           //||\\
                           '/||\'        "Archaeopteryx"
'''
shark_ascii_art = '''
                                 ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                "\""--.:-.     `.                             .:/
                  \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                   `P         `-._ \          `-:\          `. `:\
                                   ""            "            `-._)  
'''

fire_ascii_art = '''
    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
'''

gorilla_ascii_art = '''
                  ."`".
              .-./ _=_ \.-.
             {  (,(oYo),) }}
             {{ |   "   |} }
             { { \(---)/  }}
             {{  }'-=-'{ } }
             { { }._:_.{  }}
             {{  } -:- { } }
       jgs   {_{ }`===`{  _}
            ((((\)     (/))))

'''

trophy_ascii_art = '''
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\
'''

crossroads_decision = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if crossroads_decision == 'left':
    lake_decision = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake_decision == 'wait':
        doors_decision = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if doors_decision == 'red':
            print(fire_ascii_art)
            print("It\'s a room full of fire. GAME OVER.")
        elif doors_decision == 'blue':
            print(gorilla_ascii_art)
            print("You get jumped by a gorilla! GAME OVER.")
        elif doors_decision == 'yellow':
            print(trophy_ascii_art)
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn\'t exist. Game Over.")
    else:
        print(shark_ascii_art)
        print("You get attacked by a shark. GAME OVER.")
else:
    print(dino_ascii_art)
    print("You are attacked by a dinossaur. GAME OVER.")

