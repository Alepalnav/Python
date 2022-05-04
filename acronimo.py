#El usuario inserta un significado y devuelve su acrónimo.
cadena = input("Dime el significado de una organización o concepto y te digo su acrónimo:")

palabras = cadena.split(" ")

acro = ""

for p in palabras:
    acro = acro + p[0]
 
print(acro)