print("*****************************************")
print("Bem vindo ao jogo de adivinhação") #teste inicial para verificar o python em funcionamento
print("*****************************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ") #o input retorna strings, portanto devemos modificar essa entrada
#com uma função, no caso a função abaixo.

chute =int(chute_str)

print ("Você digitou : ", chute, "?")

resposta = input("Se sim digite 'sim' : ")

while(resposta != "sim"):
    chute_str = input("Digite o seu número: ")
    print("Você digitou : ", chute, "?")
    resposta = input("Se sim digite 'sim' : ")

chute = int(chute_str)

if(numero_secreto == chute ):
    print("Você acertou o número secreto !")
else:
    print("Você errou o número secreto !")
