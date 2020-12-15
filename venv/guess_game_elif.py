print("*****************************************")
print("Welcome to the guessing game") #initial test of python and pycharm
print("*****************************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ") #As the input returns only strings you have to use a function to change its type

print ("Você digitou : ", chute_str, "?")

resposta = input("Se sim digite 'sim' : ")

while(resposta != "sim"):   # Confirming with user if he actually typed that number, if he did he just have to type sim
    chute_str = input("Digite o seu número: ")
    print("Você digitou : ", chute_str, "?")
    resposta = input("Se sim digite 'sim' : ")

chute = int(chute_str) #Right here i used the function that changes the input to an int type

acertou =   chute == numero_secreto
maior   =   chute > numero_secreto
menor   =   chute < numero_secreto

if(acertou):
    print("Você acertou o número secreto !")
else:
    if(maior):
        print("Você errou o número secreto,tente um número menor.")
    elif(menor):
        print("Você errou o número secreto,tente um número maior.")


print("Fim do jogo")