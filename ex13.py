#Entrada de dados
mat = [[0,0],[0,0,]]
#Manipulação de dados
for l  in range (0,2):
    for c in range (0,2):
        mat[l][c] = int(input("Entre com valor da posição[{}][{}]".format(l,c)))
#Saida de dados
print(mat)
