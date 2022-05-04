from random import randint 

print("piedra, papel o tijeras... 1,2,3: ")

y = ["piedra", "papel", "tijeras"]

def main():

    computer = y[randint(0,2)]
    x = input("Elige: ").lower()
    print("Elección de la máquina: " + computer)

    if x == "piedra" and computer == "papel":
        print("Has perdido")
    elif x == "piedra" and computer == "tijeras":
        print("Has ganado!")
    elif x == "papel" and computer == "piedra":
        print("Has ganado!")
    elif x == "papel" and computer == "tijeras":
        print("Has perdido")
    elif x == "tijeras" and computer == "piedra":
        print("Has perdido")
    elif x == "tijeras" and computer == "papel":
        print("Has ganado!")
    else:
        print("error")
    
main()
    
