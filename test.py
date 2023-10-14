import random
aleatorio=random.randint(1,100)

cont=0

while True:
    numero=int(input("Introduce un número: "))
    if(numero<aleatorio):
        print("El número es mayor")
        cont+=1
        print("Llevas ",cont," intentos")
    elif(numero>aleatorio):
        print("El número es menor")
        cont+=1
        print("Llevas ",cont," intentos")
    else:
        print("Acertaste, los números son iguales")
        cont+=1
        print("Lo conseguiste en ",cont," intentos")
        break