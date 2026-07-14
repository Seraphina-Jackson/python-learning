# print("Welcome to Pizza deliveriess")
# size = input("What size pizza do you want ? S, M OR L ? :")
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# Olives = input("Do you want any Olives ? Y or N : ")
# if Olives == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M":
#         bill += 3
#     else :
#         bill +=3
# extra_cheese=input("Do you want extra cheese ? Y or N : ")
# if extra_cheese == "Y":
#     bill += 1
# else:
#     bill = 25

# print(f"Your final bill is : {bill}")

print("Welcome to The Oasis Of Mirage.")
print(r"""
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-')
""")               
print("Your mission is to find the treasure")
path_split = input("You start your journey on a camel. Theres a path that spilts before you. Choose your path. Do you wanna go Left or Right ? : ")
if path_split == "Left" or path_split == "left":
    print("You reach the canyon walls that provide shade and shelter. You survive.(Proceed to Step 2).")
mirage_oasis=input("You arrive at a hidden oasis, but the water looks suspiciously shimmering and blue.Do you want to drink or swim or wait ? :")
if mirage_oasis == "Drink" or mirage_oasis == "drink" and mirage_oasis == "Swim" or mirage_oasis == "swim":
    print("The water is a magical mirage or filled with hidden quicksand. Game Over!")
elif mirage_oasis == "wait" or mirage_oasis == "Wait":
    print("You wait until dusk when the heat cools down. A friendly wandering Bedouin merchant passes by and safely guides you to the entrance of the ruins. (Proceed to Step 3).") 
vault_archways = input("You stand inside the ancient tomb of the Sultan. Three decorated stone doors stand before you: Sun, Star, Shadow ; Which door do you choose: ")
if vault_archways == "sun" or vault_archways == "Sun":
    print("It triggers a trap door that drops you into a pit of desert vipers. Game Over!")
elif vault_archways =="shadow" or vault_archways =="Shadow":
    print("A gust of wind blows it shut, locking you inside forever. Game Over!")
elif vault_archways == "star" or vault_archways == "Star":
    print("it slides open to reveal the Sultan’s Eternal Flame (the treasure!). You Win!")
else:
    print("You ride straight into a massive Shamal (sandstorm). Game Over!")
