
with open("..\\..\\mates\\prueba.txt", "r") as archivo:
  lineas = archivo.readlines()
  largo = len(lineas)
  i = 0
  while i < largo:
    linea = lineas[i]
    print(linea)
    i += 1

with open("salida.txt", "a") as archivo:
  archivo.writelines(["hola buenas tardes\n", "chao buenas noches\n"])