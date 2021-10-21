#entrada de dados
vet = [[]]
n = int(input("Entre com a quantidade de numeros da lista"))
num = 1
#manipulação dos dados
for c in range (1,n+1):
    num = int(input("Digita o valor "))
    if num % 2 == 0:
        vet[0].append(num)

#saida de dados
vet[0].sort()
print(f"Seu vetor de apenas pares é {vet[0]}") 
