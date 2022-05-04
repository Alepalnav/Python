print("Bienvenido, por favor selecciona un artista de este top de dos artistas: ")
print("")
print("1. Justin Bieber")
print("2. Bad Bunny")

x = int(input())

if x == 1:
    print("Selecciona una canción de estas dos: ")
    print("")
    print("1. Baby")
    print("2. Stay")
    y = int(input())
    if y == 1:
        b = open("baby.txt", "r")
        print(b.read())
        b.close()
    if y == 2:
        s = open("stay.txt", "r")
        print(s.read())
        s.close()
    elif y > 2: 
        print("Debes elegir entre 1 y 2")
if x == 2:
    print("Selecciona una canción de estas dos: ")
    print("")
    print("1. Yonaguni")
    print("2. Dákiti")
    z = int(input())
    if z == 1:
        y = open("yonaguni.txt","r")
        print(y.read())
        y.close()
    if z == 2:
        d = open("dakiti.txt","r")
        print(d.read())
        d.close()
    elif z > 2:
        print("Debes elegir entre 1 y 2")
elif x > 2:
    print("Debes elegir entre 1 y 2")


        
    