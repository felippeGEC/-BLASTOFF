#entrada de dados
num = int(input("Entre com o numero para fatorial"))
#manipulação dos dados
cont = num
fatorial = 1
while cont > 0:
    fatorial *= cont
    cont -= 1
#saida de dados
print(fatorial)