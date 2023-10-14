n1=int(input("Introduce un número: "))
n2=int(input("Introduce hasta qué número imprimir: "))

cont=n1

while (n1<0 or n2<0):
    if n1<0:
        print("El primer número debe ser mayor a 0")
        n1=int(input("Introduce un número: "))
        cont=n1
    if n2<0:
        print("El segundo número debe ser mayor a 0")
        n2=int(input("Introduce hasta qué número imprimir: "))

while(cont<=n2):
    if(cont<n2):
        print(cont,end="-")
    else:
        print(cont,end="")
    cont=cont+1
        
#PSEUDOCÓDIGO
"""
inicio
	escribe "Introduce un número"
	lee n1
	escribe "Introduce hasta qué número imprimir"
	lee n2
	cont=n1
	mientras(n1<0 or n2<0) hacer
		si(n1<0) entonces
			escribe "El primer número debe ser mayor a 0"
			escribe "Introduce un número"
			lee n1
			cont=n1
		si(n2<0) entonces
			escribe "El segundo número debe ser mayo a 0"
			escribe "Introduce hasta qué número imprimir"
			lee n2
	mientras(cont<=2) hacer
		si(cont<n2) entonces
			escribe cont+end="-"
		sino
			escribe cont+end=""
fin
"""