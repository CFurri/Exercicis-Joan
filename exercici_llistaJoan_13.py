#13.J)

frase = ""
comptLA = 0
while frase != ".":
    frase = input("Lletra: ")
    if frase == "l":
        frase = input("Lletra: ")
        if frase == "a":
            comptLA = comptLA + 1
print(comptLA)
