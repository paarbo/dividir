divisor=int(input("Introduce el divisor: "))
quocient=int(input("Introduce el dividendo: "))
resultado=quocient%divisor
if resultado==0:
    print("Es entero")
else:
    print("No es entero")
