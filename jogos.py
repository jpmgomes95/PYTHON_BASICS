#Created this file to act like a 'menu' and to allow me create more games
import forca
import guess_game_2


print("*****************************************")
print("**************Choose a game**************") #initial test of python and pycharm
print("*****************************************")

print("(1) Guess Game     (2) Hangman")

jogo = int(input("Type the number of the game: "))

if (jogo == 1):
    print("Starting Guess Game")
    guess_game_2.play()
elif(jogo == 2):
     print("Starting Hangman")
     forca.play()

