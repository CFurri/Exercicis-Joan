# J-3.

cdvocals = 0
char = ""

while char != ".":
    char = input("Caràcter: ")
    if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        cdvocals = cdvocals + 1
print(cdvocals)
