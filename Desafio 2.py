#NUMEROS PARES
#a variavel 'pares' foi criada para fazer a escolha de um numero
pares = int(input("digite um numero"))
#o 'if' é usada como o bloco 'se; senão' do scrath. A parte '% 2 == 0' se o numero escolhido a % de 2 resultar em zero então resulta na resposta 'par'
if pares % 2 == 0:
    print("esse numero é par")
#'else é a parte 'senão' do bloco do scratch, então se a %2 não resultar em zero então ele sera 'impar'
else:
    print("esse numero é impar")
