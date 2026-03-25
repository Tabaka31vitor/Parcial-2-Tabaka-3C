#MINUTOS PARA HORA
#a variavel 'segundos' foi criada para perguntar a quantidade de segundos que deseja converter
segundos = int(input("digite a quantidade de segundos"))
#a variavel 'minutos' foi feita para fazer a conversão de segundos para minutos e conseguir mostrar a resposta abaixo
minutos = (segundos / 60)
#a variavel 'horas' foi feita para fazer a conversão de segundos para horas e conseguir mostrar a resposta abaixo
horas = (segundos / 3600)
#'print' foi criada assim para mostrar exatamente a conversão de horas e a resposta embaixo
print("horas:")
print(horas)
print("minutos:")
print(minutos)

#aqui foi feita para fazer o inverso dos segundos, no caso colocamos o valor de horas e converte em segundos e minutos
hrs = int(input("digite a quantidade de horas"))
min1 = (hrs * 60)
seg = (hrs * 3600)
print("Minutos:")
print(min1)
print("segundos")
print(seg)
