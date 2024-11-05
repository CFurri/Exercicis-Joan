#J-10:

compt = 0
frase = input("Lletra: ")
if frase == "a":
    compt = compt + 1
while frase != ".":
    frase = input("LLetra: ")
    while frase == " ":
        frase = input("Lletra: ")
        if frase == "a":
            compt = compt + 1
        
print(compt)
    

