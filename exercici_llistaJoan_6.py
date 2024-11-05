#J-6:

num_donat = int(input("Número: "))
divisor = 1

while divisor <= num_donat:
    if num_donat % divisor == 0:
        print(divisor)
    divisor = divisor + 1
        
