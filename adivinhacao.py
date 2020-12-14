print("*****************************************")
print("Welcome to the guessing game") #initial test of python and pycharm
print("*****************************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ") #As the input returns only strings you have to use a function to change its type

print ("Você digitou : ", chute_str, "?")

resposta = input("Se sim digite 'sim' : ")

while(resposta != "sim"):
    chute_str = input("Digite o seu número: ")
    print("Você digitou : ", chute_str, "?")
    resposta = input("Se sim digite 'sim' : ")

chute = int(chute_str) #Right here i used the function that changes the input to an int type

if(numero_secreto == chute ):
    print("Você acertou o número secreto !")
else:
    print("Você errou o número secreto !")
