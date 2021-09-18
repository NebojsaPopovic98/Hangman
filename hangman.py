import random
import time

print('Welcome to Hangman game! What is your name?')
name = input()
print('Hello ' + name + ', your game is about to begin!')
time.sleep(3)

def main():
    global count 
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ''
    
def play_loop(): #ponavljanje igrice nakon zavrsene partije
    global play_game
    play_game = input('Do You want to play again? y = yes, n = no \n')
    while play_game not in ('y','n','Y','N'):
        play_game = input('Do You want to play again? y = yes, n = no \n')
    if play_game == 'y' or 'Y':
        main()
    else:
        print('print("Thanks For Playing! We expect you back again!")')
        exit()
        
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input('This is the hangman word: '+ display + ' Enter your guess: \n')
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2or guess <= '9':
        print('Invalid input, try a letter.')
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |     | \n"
                  "  |  \n"
                  "  |  \n"
                  "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |  \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()