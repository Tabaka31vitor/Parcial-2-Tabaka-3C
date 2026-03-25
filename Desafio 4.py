#CALCULADORA
#'n1' e 'n2' são as variaveis criadas para selecionar os numeros
n1 = float(input("escolha um numero"))
n2 = float(input("escolha outro numero"))
#'operação' é a variavel para selecionar a operação usada
operação = input("escolha a operação:[soma, subtracao, multiplicacao, divisao]")
#'if' é para colocar as opções da escolha da operação. Então se for 'soma' realizará a primeira opção
if operação == "soma":
    print(n1+n2)
#'elif' foi usado para "se não for soma, então pode ser subtração"
elif operação == "subtracao":
    print(n1-n2)
#'elif' foi usado para "se não for soma e nem subtração, então pode ser multiplicação"
elif operação == "multiplicacao":
    print(n1*n2)
#'elif' foi usado para "se não for soma, nem subtração e nem multiplicação, então pode ser divisão"
elif operação == "divisao":
    print(n1/n2)
#'else' foi usado para caso nao seja nenhuma das operações descritas então dará a resposta "esse numero nao existe"
else:
    print("esse numero nao existe")
