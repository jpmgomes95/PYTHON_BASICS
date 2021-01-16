import  random

def  play():

    opening_message()
    secret_word = load_secret_word()
    correct_letters = load_corretct_letters(secret_word)


    hanged = False
    right = False
    mistakes = 0

    secret_word = secret_word.strip()


    while( not hanged and not right ):
        guess = ask_the_gues()

        if (guess in secret_word):
            score_right_guess(guess,correct_letters,secret_word)
        else:
            print("You have mistaken, there is'nt  {}, in this secret letter".format(guess))
            mistakes +=1

        hanged = mistakes == len(secret_word)
        right = "_" not in correct_letters
        print(correct_letters)

    if(right):
        print("Congratulations you finished the game!")
    else:
        print("You lost the game")

def opening_message():
    print("*****************************************")
    print("Welcome to the Hangman")  # initial test of python and pycharm
    print("*****************************************")


def load_secret_word():
    file = open("words.txt", "r")

    list_words = []

    for line in file:
        line = line.strip().upper()
        list_words.append(line)

    file.close()

    number = random.randrange(0, len(list_words))
    secret_word = list_words[number].upper()
    return secret_word


def load_corretct_letters(word):
    return ["_" for letter in word]


def ask_the_gues():
    guess = input("Say a letter: ")
    guess = guess.strip().upper()
    return guess

def score_right_guess(guess,correct_letters,secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            print("Congratulations you hit the letter {} in position {} ".format(guess, index))
            correct_letters[index] = guess
        index += 1



if(__name__== "__main__"):
    play()


