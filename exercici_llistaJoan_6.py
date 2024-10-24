#J-6:


num_donat = int(input("Número: "))
sequencia = num_donat

while sequencia != 0:
    num_donat = int(input("Número: "))
    x = num_donat % sequencia == 0
    
    sequencia = sequencia - 1
    
