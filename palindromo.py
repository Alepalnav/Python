print("Un palíndromo es una palabra que resulta la misma leída de izquierda a derecha que de derecha a izquierda. ")
palabras = input("Inserta 5 palabras aquí, alguna debe ser palíndromo: ")
lista = palabras.split(" ")

lista1 = list(lista[0])
lista2 = list(lista[1])
lista3 = list(lista[2])
lista4 = list(lista[3])
lista5 = list(lista[4])

if lista1[0] == lista1[-1] and lista1[1] == lista1[-2] and lista1[2] == lista1[-3] and lista1[3] == lista1[-4]:
    print(lista[0] + " es un palíndromo")
else:
    print(lista[0] + " no es un palíndromo")

if lista2[0] == lista2[-1] and lista2[1] == lista2[-2] and lista2[2] == lista2[-3] and lista2[3] == lista2[-4]:
    print(lista[1] + " también lo es")
else:
    print(lista[1] + " no es un palíndromo")

if lista3[0] == lista3[-1] and lista3[1] == lista3[-2] and lista3[2] == lista3[-3] and lista3[3] == lista3[-4]:
    print(lista[2] + " también lo es")
else:
    print(lista[2] + " no es un palíndromo")

if lista4[0] == lista4[-1] and lista4[1] == lista4[-2] and lista4[2] == lista4[-3] and lista4[3] == lista4[-4]:
    print(lista[3] + " también lo es")
else:
    print(lista[3] + " no es un palíndromo")

if lista5[0] == lista5[-1] and lista5[1] == lista5[-2] and lista5[2] == lista5[-3] and lista5[3] == lista5[-4]:
    print(lista[4] + " también lo es")
else:
    print(lista[4] + " no es un palíndromo")
    



