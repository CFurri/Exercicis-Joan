# J-15-J:

num = int(input("Número: "))
num_ant = 0
num_ant_ant = 0

while num != 0 or num > num_ant:
    num_ant_ant = num_ant
    num_ant = num
    num = int(input("Número: "))
    
if num_ant > num_ant_ant:
    print("Creixent")
else:
    print("Decreixent")




