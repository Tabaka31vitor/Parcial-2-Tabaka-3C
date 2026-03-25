#CALCULADORA
n1 = float(input("escolha um numero"))
n2 = float(input("escolha outro numero"))
operação = input("escolha a operação:[soma, subtração, multiplicação, divisão]")

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
