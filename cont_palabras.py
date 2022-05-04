#Consiste en contar las palabras de la respuesta del usuario a una pregunta
x = input("¿En qué estas pensando?")

f = open("palabras.txt","w")
f.write(x)
f.close()

f = open("palabras.txt", "r")
for x in f:                     
  y = x.split(" ")

z = len(y)
t = str(z)
print("!Muy bien, me has mostrado tu pensamiento en " + t + " palabras¡")



