#CALCULADORA
#'n1' e 'n2' são as variaveis criadas para selecionar os numeros
n1 = float(input("escolha um numero"))
n2 = float(input("escolha outro numero"))
#'operação' é a variavel para selecionar a operação usada
operação = input("escolha a operação:[soma, subtração, multiplicação, divisão]")
#'if' é para colocar 
if operação == "soma":
    print(n1+n2)
elif operação == "subtração":
    print(n1-n2)
elif operação == "multiplicação":
    print(n1*n2)
elif operação == "divisão":
    print(n1/n2)
else:
    print("esse numero nao existe")
