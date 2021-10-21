#entrada de dados
pa = str(input("Entre com a sua palavra")).upper()
#manipulação dos dados
inverso = pa[::-1]
#saida de dados
if inverso == pa:
    print("A palavra é um palidromo")
else:
    print("A palavra não é um palidromo")

