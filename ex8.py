n = int(input("Entre com o numero para ver se ele é primo"))
div = 0
for c in range (1,n+1):
   if n%c == 0:
       div +=1
if div ==2:
    print("Seu numero é primo")
else:
    print("Seu numero nao é primo")           