#Consiste en preguntar a un usuario su información personal y verificar que la información que se ha ingresado es correcta.
from datetime import datetime

nombre = input("¿Cúal es su nombre?: ")
fecha = input("¿Cúal es su fecha de nacimiento? (YYYY-MM-DD): ")
direccion = input("¿Cúal es su dirección?: ")
metas = input("¿Cúal es su meta personal?: ")

x = nombre.isalpha()

def ver_nombre():
    if x == True:
        print("- Nombre: " + nombre)
    else:
        print("- Nombre: Información incorrecta")

ver_nombre()
    
while True:
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        print("- Fecha de nacimiento: " + fecha)
    except ValueError:
        print("- Fecha de nacimiento: Fecha inválida")
    break

print("- Dirección: " + direccion)

y = metas.isalpha()

def ver_metas():
    if y == True:
        print("- Metas personales: " + metas)
    else:
        print("- Metas personales: Información incorrecta")

ver_metas()




