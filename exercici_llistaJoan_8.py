#J-8)


comptB = 0
comptC = 0
char = ""
while char != ".":
    char = input("Caràcter: ")
    if char == "b":
        comptB = comptB + 1
    elif char == "c":
        comptC = comptC + 1
if comptB > comptC:
    print("Han aparegut més Bs, en total ",comptB)
elif comptC > comptB:
    print("Han aparegut més Cs, en total ",comptC)
else:
    print("Han aparegut el mateix nombre de C's que de B's")
