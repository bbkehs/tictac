import random

def hangman():
    global placeholder
    global life
    guessed = list()
    print(f"you have {life} lives".center(64," "))
    while life != 0:
        if "-" not in placeholder:
            print("you win!".center(64," "))
            exit()
        guess = input("guesse a letter\n".center(64," "))
        if guess in guessed:
            print("Already guessed this letter!".center(64," "))
            continue
        guessed.append(guess)
        if guess not in word:
                life -=1
                print(f"{guess} is not in the word!".center(64," "))
                print(f"You have {life} lives left".center(64," "))
        else:
            print("Correct!".center(64," "))
        for i in range(0,len(word)):
            if word[i] == guess:
                ph = list(placeholder)
                ph[i] = guess
                placeholder = "".join(ph) 
        print(placeholder.center(64," "))
    else:
        print("You died!".center(64," ")) 
        exit()


def main():
    global life 
    life = 6
    global length
    global word
    global placeholder
    global guess
    
    words = ["brother","youtube","violet","desktop","comodity","headphones","hangman"]
    word =words[random.randint(0,len(words)-1)]
    
    #print(word.center(64," "))
    lenght = len(word)
    placeholder = "-"*lenght
    print(placeholder.center(64," "))

    hangman()

def play():
    global play_game
    play_game = input("Do you want to play hangman? y=yes or n=no\n".center(64," "))
    while play_game not in ["y","Y","n","N"]:
        play_game = input("Invalid! Do you want to play hangman? y=yes or n=no\n".center(64," "))
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing! cya soon".center(64," "))
        exit()
play()