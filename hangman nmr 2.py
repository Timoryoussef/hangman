
def get_word(): 
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = false 
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("lets play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter", guess
            elif guess not in word:
                print(guess, "is  not in the word. ")
        elif len(guess) == len(word) and guess.isalpha():
            
        
        else:
            print("not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        