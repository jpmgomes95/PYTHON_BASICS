import  random

def  play():
    print("*****************************************")
    print("Welcome to the Hangman") #initial test of python and pycharm
    print("*****************************************")

    file = open("words.txt", "r")

    list_words= []

    for line in file:
        line = line.strip().upper()
        list_words.append(line)

    file.close()

    number = random.randrange(0,len(list_words))
    secret_word = list_words[number].upper()

    correct_letters = ["_" for letter in secret_word]

    hanged = False
    right = False
    mistakes = 0

    secret_word = secret_word.strip()

    while( not hanged and not right ):

        guess =  input("Say a letter: ")
        guess = guess.strip().upper()

        if (guess in secret_word):
            index = 0
            for letter in secret_word :
                if (guess == letter):
                    print("Congratulations you hit the letter {} in position {} ".format(guess, index))
                    correct_letters[index] = guess

                index += 1
        else:
            print("You have mistaken, there is'nt  {}, in this secret letter".format(guess))
            mistakes +=1

        hanged = mistakes == 6
        right = "_" not in correct_letters
        print(correct_letters)

    if(right):
        print("Congratulations you finished the game!")
    else:
        print("You lost the game")


if(__name__== "__main__"):
    play()