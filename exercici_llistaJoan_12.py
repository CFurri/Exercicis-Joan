#12.J-a)

val_donat = int(input("Valor donat: "))
serie = int(input("Número: "))
comp = True
if serie == val_donat:
    print("El valor pertany a la seqüència")
else:
    while not (serie == 0) and (serie != val_donat):
        serie = int(input("Número: "))
        if serie == val_donat:
            comp = False
    if comp == False:
        print("El valor donat pertany a la seqüència.")
    else:
        print("El valor donat no apareix a la seqüència.")
    
        

