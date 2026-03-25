#TAXA DE JUROS
#'c' é a variavel para o valor da capital
c = float(input("digite o valor de capital"))
#'i' é a variavel para o valor da taxa 
i = float(input("digite o valor de i"))
#'t' é a variavel para o valor do tempo
t = float(input("digite o valor de t"))

#'j' é uma variavel criada para conseguir ser impressa a resposta depois. E também foi criada para conseguir fazer o resultado da fórmula dos juros
j = (c*i*t) /100
#print é só para mostrar a resposta para o usuario
print(j)
