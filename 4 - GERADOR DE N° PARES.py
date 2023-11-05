#GERADOR DE NUMEROS PARES

a = int(input("Gerador de números pares:\n Qual seu número de inicio?\n"))
b= int(input("Ate quanto?"))

if b%2 == 0:
  b +=1
else:
  b=b

if a%2 != 0:
  a += 1 
  for x in range(a, b, 2):
    print(x)

else:
   for x in range(a, b, 2):
     print(x)