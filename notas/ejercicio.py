
# BLOQUE DE DEFINICION
# Bloque de importaciones
# No hay

# Definición de constantes
NOMBRE_ARCHIVO_RESPUESTAS = "respuestas.txt"

# Definición de funciones

def leer_archivo(nombre_archivo, separador):
  """"
  Lee un archivo y separa las líneas según el separador
  Entrada: nombre del archivo y separador de datos
  Salida: Lista de listas con las líneas separadas
  """
  contenido_archivo = []
  with open(nombre_archivo, "r") as archivo:
    lineas = archivo.readlines()
    largo = len(lineas)
    i = 0
    while i < largo:
      linea = lineas[i]
      linea_separada = linea.split(separador)
      contenido_archivo.append(linea_separada)
      i += 1
  return contenido_archivo

def escribir_resultados(resultados, puntaje, nota):
  """"
  Crea el archivo con los resultados de la evaluación con los datos entregados
  Entrada: lista de listas con los resultados del estudiante, puntaje obtenido y nota
  Salida: archivo con estos resultados escritos
  """
  with open("resultados_estudiante.txt", "w") as archivo:
    largo = len(resultados)
    i = 0
    while i < largo:
      resultado = resultados[i]
      archivo.write(resultado[0] + ":" + resultado[1].strip() + "->" + resultado[2] + "\n")
      i += 1
    archivo.write("\nPuntaje obtenido: " + str(puntaje) + " / 100\n")
    archivo.write("Nota obtenida: " + str(nota))

def calcular_resultados(respuestas_estudiante, respuestas_correctas):
  """
  Verifica si las respuestas del estudiante están correctas, calculando puntaje y nota
  Entrada: lista de listas con las respuestas del estudiante y lista de listas con las respuestas correctas
  Salida: archivo con los resultados escritos
  """
  resultados = []
  i = 0
  puntaje = 0
  largo = len(respuestas_estudiante)
  while i < largo:
    estudiante = respuestas_estudiante[i]
    correcta = respuestas_correctas[i]
    resultado = "INCORRECTA"
    if estudiante[1].strip() == correcta[1].strip():
      resultado = "CORRECTA"
      puntaje += int(correcta[2])
    lista_resultado = [estudiante[0], estudiante[1], resultado]
    resultados.append(lista_resultado)
    i += 1
  nota = round(1 + puntaje * 6 / 100, 1)
  escribir_resultados(resultados, puntaje, nota)

# BLOQUE PRINCIPAL

# Entrada
nombre_archivo = input("Ingrese nombre del archivo con las respuestas del estudiante: ")

# Procesamiento

respuestas_estudiante = leer_archivo(nombre_archivo, ":")
respuestas_correctas = leer_archivo(NOMBRE_ARCHIVO_RESPUESTAS, ";")

# Salida

calcular_resultados(respuestas_estudiante, respuestas_correctas)