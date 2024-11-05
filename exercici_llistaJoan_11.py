 #J-11)


serie = int(input("Número: "))
comprovacio = False
if serie == 0:
    print("No hi ha sèrie.")
else:
    while not (serie == 0) and (comprovacio == False):
        serie = int(input("Número: "))
        if serie < 0:
            comprovacio = True
    if comprovacio == True:
        print("Hi ha un negatiu.")
    else:
        print("No hi ha negatius.")
