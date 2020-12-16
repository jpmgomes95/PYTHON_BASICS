import random

print("*****************************************")
print("Welcome to the guessing game") #initial test of python and pycharm
print("*****************************************")

numero_secreto = random.randrange(1,101) #Created a secret number, so every game should be unique
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade ?")
print("(1)  Fácil   (2)  Médio   (3)  Difícil")

nivel = int(input("Escreva o número do nível: "))



if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
elif (nivel == 3):
    total_de_tentativas =  5
else:
    print("Você não digitou um nível válido")


for rodada in range(1, total_de_tentativas +1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ") #As the input returns only strings you have to use a function to change its type
    print("Você digitou : ", chute_str,)
    chute = int(chute_str) #Right here i used the function that changes the input to an int type

    if(chute <1 or chute >100):
        print("você deve digitar um número entre 1 e 100")
        continue

    acertou =   chute == numero_secreto
    maior   =   chute > numero_secreto
    menor   =   chute < numero_secreto

    if(acertou):
        print("Você acertou o número secreto e fez {} pontos!".format(pontos))
        break #If the user guess the number, the game finishes instatly
    else:
        if(maior):
             print("Você errou o número secreto, você chutou um número grande de mais.")
        elif(menor):
             print("Você errou o número secreto, você chutou um número pequeno de mais")

       pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo, você fez {} pontos !".format(pontos))