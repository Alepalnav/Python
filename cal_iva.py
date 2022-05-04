x = int(input("Cuál es la factura total de hoy sin iva? "))

porcentaje = 21 * x/100

total = x + porcentaje 

print("El iva es " + str(porcentaje) + " y el total con iva es " + str(total))

y = int(input("Cuántas personas sois?"))

rep = total/y 

print("La cantidad que tiene que pagar cada uno es " + str(rep))
