#J-5:

compt = 0
sumatori = 0
serie = int(input("Número: "))

while serie != 0:
    sumatori = sumatori + serie
    compt = compt + 1
    serie = int(input("Número: "))
    
print(sumatori/compt)

