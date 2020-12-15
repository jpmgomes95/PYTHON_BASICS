print("*****************************************")
print("Welcome to the guessing game") #initial test of python and pycharm
print("*****************************************")

numero_secreto = 42
total_de_tentativas = 3

while (total_de_tentativas > 0):
    print("Você possui", total_de_tentativas,"tentativa(s) restante(s)")
    chute_str = input("Digite o seu número: ") #As the input returns only strings you have to use a function to change its type

    print ("Você digitou : ", chute_str,)

    chute = int(chute_str) #Right here i used the function that changes the input to an int type

    acertou =   chute == numero_secreto
    maior   =   chute > numero_secreto
    menor   =   chute < numero_secreto

    if(acertou):
        total_de_tentativas = total_de_tentativas -3
        print("Você acertou o número secreto !")
    else:
        total_de_tentativas = total_de_tentativas -1
        if(maior):
             print("Você errou o número secreto,tente um número menor.")
        elif(menor):
             print("Você errou o número secreto,tente um número maior.")


print("Fim do jogo")