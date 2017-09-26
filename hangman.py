import random


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secret_word:
        if i in letters_guessed:
            continue
        else:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    lngth = len(secret_word)
    secret_word_guesses = []
    for i in range(0, lngth):
        secret_word_guesses.append('_')

    for i in letters_guessed:
        if i in secret_word:
            for x in range(0, lngth):
                if secret_word[x] == i:
                    secret_word_guesses[x] = i

    if letters_guessed[-1] not in secret_word:
        print("That letter is not in the secret word.")
    else:
        print("That letter is in the secret word.")

    return secret_word_guesses


def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in letters_guessed:
        alphabet.remove(i)

    unguessed_letters = ""
    for i in alphabet:
        unguessed_letters = unguessed_letters + i
    print(unguessed_letters)

    return unguessed_letters


def print_hangman(number_of_guesses):
    if number_of_guesses == 0:
        print("      _____       ")
        print("     |     |      ")
        print("     |            ")
        print("     |            ")
        print("     |            ")
        print("     ========     ")
    elif number_of_guesses == 1:
        print("      _____       ")
        print("     |     |      ")
        print("     |     O      ")
        print("     |            ")
        print("     |            ")
        print("     ========     ")
    elif number_of_guesses == 2:
        print("      _____       ")
        print("     |     |      ")
        print("     |     O      ")
        print("     |     |      ")
        print("     |            ")
        print("     ========     ")
    elif number_of_guesses == 3:
        print("      _____       ")
        print("     |     |      ")
        print("     |     O      ")
        print("     |     |      ")
        print("     |     /      ")
        print("     ========     ")
    elif number_of_guesses == 4:
        print("      _____       ")
        print("     |     |      ")
        print("     |     O      ")
        print("     |     |      ")
        print("     |     /\     ")
        print("     ========     ")
    elif number_of_guesses == 5:
        print("      _____       ")
        print("     |     |      ")
        print("     |     O      ")
        print("     |    -|      ")
        print("     |     /\     ")
        print("     ========     ")
    elif number_of_guesses == 6:
        print("      _____       ")
        print("     |     |      ")
        print("     |     O      ")
        print("     |    -|-     ")
        print("     |     /\     ")
        print("     ========     ")

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lngth = len(secret_word)
    print("The secret word contains " + str(lngth) + " letters.")

    game_over = False
    guessed_letters = []
    correct_guessed_letters = []

    print_hangman(0)

    while not game_over:
        if len(guessed_letters) > 0:
            available_letters = get_available_letters(guessed_letters)
            print_hangman(26 - len(available_letters))
            print("Guessed letters: " + str(guessed_letters))
            print("Available letters: " + str(available_letters))
            print("Correct letters: " + str(correct_guessed_letters) + "\n")

        if 26 - len(get_available_letters(guessed_letters)) == 6:
            print("YOU LOSE")
            return

        input_letter = input("Guess a letter: ")

        if len(input_letter) > 1:
            print("Please enter one letter only.")
            continue

        if input_letter in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(input_letter)
        correct_guessed_letters = get_guessed_word(secret_word, guessed_letters)
        game_over = is_word_guessed(secret_word, guessed_letters)

    print("\nYou Win!")
    print("The secret word was \"" + secret_word + "\"")

secret_word = load_word()
hangman(secret_word)
