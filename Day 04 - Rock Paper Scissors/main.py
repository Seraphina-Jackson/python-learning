# Heads or Tails (Randomisation)
# import random
# random_heads_tails = random.randint(a=0,b=9)
# if random_heads_tails == 0 :
#     print("Heads")
# else :
#     print("Tails")
#--------------------------------------------------------------
#Banker Roulette
# import random
# friends = ["Serra", "TinkerBella", "Charlie"]
# random_pay = random.choice(friends)
# print(random_pay)
#---------------------------------------------------------------
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
# print(dirty_dozen)
# print(dirty_dozen[0])
#----------------------------------------------------------------
import random
print("Ready to win or lose in this game of Rock, Paper and Scissors?")
user_input = input("What do you choose ? Type 0 for Rock, 1 for paper and 2 for scissors : ")
if user_input == "0":
    print(r""" 
"!!!ROCK IT, MAN!!!
 !!!GO, MAN, GO!!!"                       _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
           /---._.---._.---\        /       /
           \||   '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/ """)
    
elif user_input == "1":
    print(r"""  _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|       """)
else  :
    print(r"""  _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.""")
    
print("bot chose")
choices = ["Rock","Paper","Scissors"]
random_choose = random.choice(choices)
if random_choose == "Rock":
    print(r"""   "!!!RIGHT ON MAN!!! KEEP PLAYIN' IT, MAN!!!
    HEAVV-EE!!! KEEP IT HEAVY, MAN!!! KEEP IT HEAVY!!!"
              \
 _____         \
| | | |/\       \
|_|_|_|\ \       \
|        /
\_______/            (  ( ) ) ( )  )
 \______\           ( ( ( ( )  )  ) )
 \       \         ( ( )) ) (   ) ( ( )
  \       \        ( (__.-.___.-.__) )
   \       \        /---._.---._.--- \
    \       \       \||   '  \'    ||/
     \       \       |||     _)   |||
      \       \       ||||///\\\||||
       \       \_____/ ||||\__/||||\___
        \             \ |||||||||| /   \
         \             \  ||||||  /     \
          \_____
          """)
elif random_choose == "Paper":
    print(r"""  _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| """)
else :
    print(r"""           _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
                                   
                                    """)
    
if random_choose == "Rock" and user_input == "1":
    print("You win")
elif random_choose == "Paper" and user_input == "0":
    print("Bot wins")
elif random_choose == "Rock" and user_input == "2":
    print("Bot wins")
elif random_choose == "Scissors" and user_input == "0":
    print("You win")
elif random_choose == "Paper" and user_input == "2":
    print("You win")
elif random_choose == "Scissors" and user_input == "1":
    print("Bot wins")
else :
    print("Its a tie")



