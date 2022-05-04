#Comprobar si el numero introducido es par o impar

x = int(input("¿En qué número estás pensando?"))               #Se muestra un mensaje y el usuario escribe el numero que piensa(x)

def par_impar():                                               #Esta funcion trata de adivinar si x es par o impar pregunta un segundo numero(y)
    if (x % 2) == 0:
        print("Es un número par! Puedes añadir otro?")
    else:
        print("Es un número impar! Puedes añadir otro?")
    
par_impar()

y = int(input())

def par_impar2():                                             # Esta función trata de adivinar el segundo número y vuelve a preguntar otro numero 
    if (y % 2) == 0:
        print("Es un número par! ")
    else:
        print("Es un número impar! ")

    
par_impar2()


