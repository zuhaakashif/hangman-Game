import random #to choose randomly from the word list
from words import words #we import words from a file in which we've stored 2500+ random words inside a dictionary that is also called words
import string
from hangman_visual import lives_visual_dict #we created another dictionary in a separate file that gives a visual demonstration of the hangman each time the user loses a life

def get_valid_word(words): #we store the list of words inside a function called get_valid_word
    word = random.choice(words) #randomly chooses a word from the list
    while '-' in word or ' ' in word: #it would be difficult to guess a word with a dash or space in it so we create a while loop that keeps iterating until we get a word
        word = random.choice(words)   #that doesn't contain a dash or a space

    return word.upper()  #we will return the word that has been randomly chosen and and convert it into uppercase

def hangman(): #we need to keep track of which letters we've guessed and which ones we've CORRECTLY guessed in the word
    word = get_valid_word(words)
    word_letters = set(word)      #we create a set that stores all the letters in the word
    alphabet = set(string.ascii_uppercase) #importing a set of alphabets in the dictionary
    used_letters = set()          #we create a set that stores all the letters that the user has guessed


    #we give the user 7 chances to guess the word
    lives = 7

    #we create a while loop that will keep iterating and taking input from the user until the the user has not correctly guessed the word which means
    #that the until the length of the letters in the word is greater than 0 AND the lives the user still has is also greater than 0, the loop will keep running
    while len(word_letters) > 0 and lives > 0:
        #we need to tell the user that they have this amount of lives left and that they have guessed these letters so we create a print statement
        #we also use the join method to take the used letters that are stored in the set to create them into a string separated by a space
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        #we need to tell the user the current word so we create a list that shows a letter for the letter that the user has guessed
        #and a dash for the ones that they have not guessed yet
        word_list = [letter if letter in used_letters else '_' for letter in word]
        #we will also print the visual hangman that will show a certain graphic according to how many lives the user has left
        print(lives_visual_dict[lives])
        #we print the current word by converting into a string using the join method
        print('Current word: ', ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper() #to get input from the user and convert it to uppercase
        if user_letter in alphabet - used_letters: #the user inputs something and if this is a valid alphabet that the user hasn't guessed yet, then
            used_letters.add(user_letter)          #we will add that letter to the the used letters set
            if user_letter in word_letters:
                word_letters.remove(user_letter)   #if the user correctly guesses a letter, then we remove that letter from word_letters
            else:
                lives = lives - 1    #else if the user has incorrectly guessed a letter, we take one life from the user
                print('Letter is not in the word.')

        elif user_letter in used_letters:                                     #if the user inputs a letter and it's already been used
            print('You have already used that character. Please try again.')
        else:                                                                 #and if the user inputs something that is not in the alphabet
            print('Invalid character. Please try again.')

    # we will exit the while loop if the user has failed to guess the word and the lives = 0 and tell them what the word was
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    # and if the lives are not equal to 0 and the user has correctly guessed the word, we will print the following statement
    else:
        print('You guessed the word', word, '!!')


# we call the hangman function we created earlier to run the program
hangman()
