from random import randint

num = randint(1,50)
x = int(input("Inserte un número entre 1 y 50: "))

while x != num:
    if x < num:
        print("Intenta con un número mas alto: ")
        x = int(input())
    else: 
        print("Intenta con un número mas bajo: ")
        x = int(input())

print("Lo has acertado!")







        
        

