isWinning = False

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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welcome to the quest to Treasure Island.\nYour mission is to find the treasure.")

while True:
    print("\nYou are at a crossroad. Where do you want to go? Be careful in what you wish for, adventurer.")
    print('''   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣉⣉⣁⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

    direction = input("Type 'LEFT' or 'RIGHT'.\n>>> ")

    if (direction.lower() == "left"):

        print("\nYou have reached the great lake. There is an island in the middle of it.\nGo, answer your calling.")

        print('''
         ___ __ 
        (_  ( . ) )__                  '.    \   :   /    .'
          '(___(_____)      __           '.   \  :  /   .'
                          /. _\            '.  \ : /  .'
                    .--.|/_/__      -----____   _  _____-----
     _______________''.--o/___  \_______________(_)___________
             ~        /.'o|_o  '.|  ~                   ~   ~
       ~            |/    |_|  ~'         ~
                    '  ~  |_|        ~       ~     ~     ~
          ~    ~          |_|O  ~                       ~
                 ~     ___|_||_____     ~       ~    ~
       ~    ~      .'':. .|_|A:. ..::''.
                 /:.  .:::|_|.\ .:.  :.:\   ~
      ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
                 \.: .:  :. .: ..:: .lcf/
        ~      ~      ~    ~    ~         ~
                   ~           ~    ~   ~             ~
            ~         ~            ~   ~                 ~
       ~                  ~    ~ ~                 ~
              ''')

        swim_choice = input("\nType 'WAIT' to wait for a boat. \nType 'SWIM' to swim across.\n>>> ")

        if (swim_choice.lower() == "wait"):

            print("\nCongrats, you have reached the island unharmed.")

            print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⡇⢸⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⠿⠿⠉⣉⣉⠙⠿⠿⠇⠸⠿⠿⠋⣉⣉⠉⠿⠿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⠀⣶⠀⣿⣿⢰⣶⣶⣶⣶⣶⣶⡆⣿⣿⠀⣶⠀⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣤⣤⠀⠛⠛⢀⣤⣤⡄⢠⣤⣤⡀⠛⠛⠀⣤⣤⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀''')

            door_color = input("\nThere is a house with 3 doors. One RED, one BLUE, one YELLOW.\nWhich do you choose? Your choice only can decide your fate.\n>>> ")

            if (door_color.lower() == "red"):
                print("\nYou entered a room full of fire. Adios! GAME OVER :(")
            elif (door_color.lower() == "blue"):
                print("\nYou entered a room full of beasts. Good bye! Game Over :(")
            elif (door_color.lower() == "yellow"):
                print("\nYEAAAAAAAAHHHHHH!!!!!!! You just won the game :)")
                
                print('''⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠂⠀⠀⠀
⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀
⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⣠⣾⣰⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⢀⡔⢀⣴⣶⣶⡄⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀
⢠⣿⣿⣿⣿⡿⠟⠛⠙⠛⢿⡀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣠⣾⣷⣿⣿⣿⣿⡁⠀⠀⢰⣿⡇⢀⣴⠂⠀⠀
⣸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡏⢠⣿⡇⠀⠀⠀⠀⠀⠀⢿⣿⠋⣱⣿⣿⠛⣿⡆⠀⣸⣿⣶⣿⣿⣶⣿⣷
⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣤⡀⣿⣿⡇⢸⣿⠀⠀⣴⣿⣿⣷⢀⣼⣿⠀⠻⠿⠃⠀⣿⣿⣾⣿⣿⠛⣻⣿⠟⠉⠋
⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⢿⣿⣿⣿⣿⡇⢸⣿⣆⣸⣿⠟⢿⣿⣿⠇⣿⠀⢀⣴⣶⣿⣿⣯⠀⣿⡏⠀⢹⣿⡀⠀⠀
⠀⢿⣿⣿⣿⣦⣤⣤⣤⣴⣾⣿⣿⡟⠀⠈⢿⣿⣿⣿⠁⠸⣿⣿⣿⣿⠀⠸⣿⡟⢸⣿⡄⣿⡏⠁⣸⣿⣿⣀⣿⡇⣄⡀⠻⣷⣤⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣷⠀⠀⢸⣿⣿⢿⠀⠀⠻⣿⣿⣿⡄⣸⣿⢃⣿⣿⡇⣿⣧⣶⣿⢿⣿⣿⣿⡇⢹⣿⡁⣹⣿⣷
⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⣿⣿⣿⣧⣴⣿⣿⡟⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⠚⠉⠙⠓⠈⠉⠉⠀⠀⠉⠙⣿⣷⡀⢿⣿⣿⣿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⠟⠀⠀⣠⣿⠀⠀⠀⠉⠉⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣄⡈⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠠⣾⣿⣿⣧⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡖⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣧⡀⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡁⠀⠀⠀''')
                
                break
            else:
                print("\nInvalid input. Game Over :(")
                        
        elif (swim_choice.lower() == "swim"):
            print("\nYou were attacked by a trout. Game Over.")
        else:
            print("\nInvalid input. \nGame over :(")

    elif (direction.lower() == "right"):
        print("\nYou fell into a hole. \nSorry, game over :(")       
    else:
        print("\nInvalid input. \nGame over :( \nTry Again?")
    
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⣶⡆⠀⣰⣿⠇⣾⡿⠛⠉⠁
⠀⣠⣴⠾⠿⠿⠀⢀⣾⣿⣆⣀⣸⣿⣷⣾⣿⡿⢸⣿⠟⢓⠀⠀
⣴⡟⠁⣀⣠⣤⠀⣼⣿⠾⣿⣻⣿⠃⠙⢫⣿⠃⣿⡿⠟⠛⠁⠀
⢿⣝⣻⣿⡿⠋⠾⠟⠁⠀⠹⠟⠛⠀⠀⠈⠉⠀⠉⠀⠀⠀⠀⠀
⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣀⢀⣠⣤⣴⣤⣄⠀
⠀⠀⠀⠀⣀⣤⣤⢶⣤⠀⠀⢀⣴⢃⣿⠟⠋⢹⣿⣣⣴⡿⠋⠀
⠀⠀⣰⣾⠟⠉⣿⡜⣿⡆⣴⡿⠁⣼⡿⠛⢃⣾⡿⠋⢻⣇⠀⠀
⠀⠐⣿⡁⢀⣠⣿⡇⢹⣿⡿⠁⢠⣿⠷⠟⠻⠟⠀⠀⠈⠛⠀⠀
⠀⠀⠙⠻⠿⠟⠋⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')    
    print("\nDo you wish to start again?")
    restart = input("Type 'Y' or 'N'.\n>>> ")
    if (restart.upper() == "N"):
        print("\nAdios!!!")
        break
    