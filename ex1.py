#entrada de dados
media = 0
#manipulação dos dados
for c in range (1,6):
    id = int(input("Entre com a idade da {} pessoa".format(c)))
    media = id + media
#saida de dados
print("A media de idades foi :", media/5)