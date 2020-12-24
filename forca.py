def  play():
    print("*****************************************")
    print("Welcome to the Hangman") #initial test of python and pycharm
    print("*****************************************")

    secret_word = "banana"
    hanged = False
    miss = False

    secret_word = secret_word.strip()

    while( not hanged and not miss ):

        guess =  input("Say a letter: ")
        guess = guess.strip()

        index = 0

        for letter in secret_word :
            if (guess.lower() == letter.lower()):
                print("Congratulations you hit the letter {} in position {} ".format(guess, index))
            index = index + 1



    print("End game")

if(__name__== "__main__"):
    play()