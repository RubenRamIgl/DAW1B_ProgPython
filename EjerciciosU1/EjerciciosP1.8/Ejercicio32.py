x=int(input("Introduce un número: "))
y=int(input("Introduce otro: "))

if(x<=y):
    numIni=x
    numFin=y
else:
    numIni=y
    numFin=x

while(numIni<=numFin):
    print(numIni,end="")
    if(numIni!=numFin):
        print("-",end="")
    numIni=numIni+1