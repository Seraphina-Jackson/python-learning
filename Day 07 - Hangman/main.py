import random

word_list = ["laptop","bottle","mouse"]
chosen_word = random.choice(word_list)

gussed_letters = []

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
    
print("Guess the word :" , {placeholder})

game_over = False

while not game_over:
    guess = input("Guess a letter : ").lower()
    
    if guess in chosen_word:
        print("You guessed it right, guess the next!")
        gussed_letters.append(guess)
    else:
        print("You guessed", guess ,"that's not in the word. You lose a life.")
    
    display = ""
    for letter in chosen_word :
        if letter == guess or letter in gussed_letters:
            display += letter
        else:
            display += "_"           
    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win")
    
    
        




    
    