#J-7:

nombre = int(input("Nombre: "))
div = 2
while nombre%div != 0:
    div = div + 1

if div == nombre:
    print("És un nombre primer.")
else:
    print("No és un nombre primer.")

    
