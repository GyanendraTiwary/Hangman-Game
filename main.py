import random
import hangman_word_art
import hangman_words
import clear_screen

choice = 1

while choice == 1:
    print(hangman_word_art.logo) #printing the logo


    lives = 6  # no of unsuccessfull attempts

    chosen_word =  random.choice(hangman_words.word_list) # choising the random word

    length_chosen_word = len(chosen_word)   # calculating length of the chosen word

    
    the_word = []      # making a list for the word chosen 


    # loop for creating blank spaces for each letter in the chosen word
    for i in range(length_chosen_word):
        the_word.append('_')

    print(the_word)



    end_of_game = False  # boolean for checking if the game is ended


    # loop unitl the game is ended
    while not end_of_game:
        guess = input("Guess a letter: ").lower() #taking letter input from the user
        found = False; # boolean to check if the letter is found

        # loop to compare user input with each letter in the chosen word
        for position in range(length_chosen_word):
            if guess == chosen_word[position]:
                the_word[position] = guess
                found = True
        # if letter found then replacing the blank space with letter
        if found:
            clear_screen.clear() #statement to clear the screen before printing anything
            print("Going Good, You are a Saviour !!!")
            print(the_word)
        # else decreasing the life and printing art accoeding to the lives left
        else:
            clear_screen.clear() 
            print(the_word)
            print("Keep Trying, you can save a life..")
            print(hangman_word_art.stages[lives])
            lives -= 1
        
        # if life is equal to zero printing hanged man and setting end_of_game boolean to true
        if lives == 0:
            clear_screen.clear()
            end_of_game = True
            print(hangman_word_art.stages[0])
            print("HANGMAN")
        # if all spaces are filled then ending the game and printing you win..
        if not '_' in the_word:
            end_of_game = True
            print("You Win !!!")

    choice = int(input("To play again press 1 , any other number to exit"))