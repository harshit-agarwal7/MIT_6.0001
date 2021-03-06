# Problem Set 2, hangman.py
# Name: Harshit Agarwal
# Collaborators:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    """ Returns whether the secret word is already guessed.
        A loop is executed to extract each character of the secret_word
        and then it is checked whether that character is any of the letters
        that we have guessed. """
    for char in secret_word:
        flag = False
        for letter in letters_guessed:
            if char == letter:
                flag = True
        if flag == False:
            break

    return flag


def get_guessed_word(secret_word, letters_guessed):
    corr_word = []
    for i in range(len(secret_word)):       # Creates a list that has as many underscores as the length of the secret word
        corr_word.append('_')
    for letter in letters_guessed:          # A loop is run through the list 'letters_guessed' and each element of the list is compared with the characters of the secret word. If element and the character are equal
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                corr_word[i] = letter
    corr_word1 = ''
    for element in corr_word:
        if element == '_':
            corr_word1 += element + ' '
        else:
            corr_word1 += element
    return corr_word1


def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    for letter in letters_guessed:
        for i in range(len(letters_left)):
            if letters_left[i] == letter:
                letters_left = letters_left[0:i] + letters_left[i+1:len(letters_left)]
                break
    return letters_left

def hangman(secret_word):
    i = 0
    j = 6
    k = 3
    for char in secret_word:
        i = i + 1
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is %s letters long' %i
    print '-----------'
    letters_guessed = []
    while j > 0:
        print 'You have %s warnings left' %k
        print 'You have %s guesses left' %j
        print 'Available letters: ' + get_available_letters(letters_guessed)
        x = raw_input("Please guess a letter: ")
        if str.isalpha(x) == True:
            x = str.lower(x)

        if (str.isalpha(x) == False and k > 0) or (x in letters_guessed and k > 0):
            k = k - 1
            print 'Oops! That is not valid letter. You have %d warnings left: %s' % (k, get_guessed_word(secret_word, letters_guessed))
        elif (str.isalpha(x) == False and k == 0) or (x in letters_guessed and k == 0):
            j = j - 1
            print 'Oops! That is not valid letter. You have %d guesses left: %s' % (j, get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(x)
            if x in secret_word:
                print 'Good guess: ' + get_guessed_word(secret_word, letters_guessed)
            else:
                print 'Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed)
                if x in 'aeiou':
                    j = j - 2
                else:
                    j = j - 1
        print '-----------'
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print 'Congratulations! You have won the game'
            total_score = j * len(letters_guessed)
            print 'Your total score for this game is %s' %total_score
            break
    if get_guessed_word(secret_word, letters_guessed) != secret_word:
        print 'Sorry, you ran out of guesses, the word was %s' %secret_word






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    flag = True
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        flag = False
    else:
        for i in range(0, len(my_word)):
            if my_word[i] == '_':
                flag = True
            else:
                if my_word[i] != other_word[i]:
                    flag = False
                    break
    return flag


    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist:
       c = 0
       if match_with_gaps(my_word, word) == True:
           print word
           c = c + 1


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    i = 0
    j = 6
    k = 3
    for char in secret_word:
        i = i + 1
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is %s letters long' %i
    print '-----------'
    letters_guessed = []
    while j > 0:
        print 'You have %s warnings left' %k
        print 'You have %s guesses left' %j
        print 'Available letters: ' + get_available_letters(letters_guessed)
        x = raw_input("Please guess a letter: ")
        if str.isalpha(x) == True:
            x = str.lower(x)

        if (str.isalpha(x) == False and k > 0 and x != '*') or (x in letters_guessed and k > 0):
            k = k - 1
            print 'Oops! That is not valid letter. You have %d warnings left: %s' % (k, get_guessed_word(secret_word, letters_guessed))
        elif (str.isalpha(x) == False and k == 0 and x != '*') or (x in letters_guessed and k == 0):
            j = j - 1
            print 'Oops! That is not valid letter. You have %d guesses left: %s' % (j, get_guessed_word(secret_word, letters_guessed))
        elif x == '*':
            print show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(x)
            if x in secret_word:
                print 'Good guess: ' + get_guessed_word(secret_word, letters_guessed)
            else:
                print 'Oops! That letter is not in my word: ' + get_guessed_word(secret_word, letters_guessed)
                if x in 'aeiou':
                    j = j - 2
                else:
                    j = j - 1
        print '-----------'
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print 'Congratulations! You have won the game'
            total_score = j * len(letters_guessed)
            print 'Your total score for this game is %s' %total_score
            break
    if get_guessed_word(secret_word, letters_guessed) != secret_word:
        print 'Sorry, you ran out of guesses, the word was %s' %secret_word



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
