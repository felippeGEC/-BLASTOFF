#Entrada de dados
a = int(input("Entre com o primeiro valor"))
b = int(input("Entre com o segundo valor"))
c = int(input("Entre com o terceiro valor"))
#Manipulação de dados
m = a
if b<a and b>c:
     m = b 
if c<a and c<b:
    m = c  

#Saida de dados 
print("O menor valor foi {}".format(m))