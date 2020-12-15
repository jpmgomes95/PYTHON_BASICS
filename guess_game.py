print("*****************************************")
print("Welcome to the guessing game") #initial test of python and pycharm
print("*****************************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ") #As the input returns only strings you have to use a function to change its type

    print ("Você digitou : ", chute_str,)

    chute = int(chute_str) #Right here i used the function that changes the input to an int type

    acertou =   chute == numero_secreto
    maior   =   chute > numero_secreto
    menor   =   chute < numero_secreto

    if(acertou):
        print("Você acertou o número secreto !")
    else:
        if(maior):
             print("Você errou o número secreto, você chutou um número grande de mais.")
        elif(menor):
             print("Você errou o número secreto, você chutou um número pequeno de mais")

    rodada = rodada + 1

print("Fim do jogo")