#12.J-b)

val_donat = int(input("Valor donat: "))
serie = int(input("Número: "))

if serie == val_donat:
    print("El valor pertany a la seqüència")
else:
    while not ((serie == 0) or (serie != val_donat) or (comp1 == True)):
        serie = int(input("Número: "))
        if serie == val_donat:
            comp = False
        elif val_donat < serie:
            comp1 = False
    if comp == False:
        print("El valor donat pertany a la seqüència.")
    elif comp1 == False:
        print("El valor donat no apareix a la seqüència.")
    else:
        print("El valor donat no apareix a la seqüència.")
