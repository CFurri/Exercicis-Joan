#14-J)

frase = ""
comptLA = 0
comptAL = 0

while frase != ".":
    frase = input("Lletra: ")
    while frase == "l":
        frase = input("Lletra: ")
        if frase == "a":
            comptLA = comptLA + 1
    while frase == "a":
        frase = input("Lletra: ")
        if frase == "l":
            comptAL = comptAL + 1
print("Hi ha ",comptLA," aparicions de 'la' i ",comptAL, "aparicions de 'al'.")
