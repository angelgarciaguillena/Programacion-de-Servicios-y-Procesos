from multiprocessing import Lock, Pool
import random
import time

lock = Lock()

def generarNumero(fichero):

    f = open(fichero, 'w')
    notas = []
    
    with open(fichero, 'w') as f:
        for i in range(6):
            numero = random.randint(1, 10)
            f.write(f"{numero}\n")
            notas.append(numero)

    f.close()
    return notas


def calcularMedia(ficheroLectura, ficheroEscritura, alumno):

    f1 = open(ficheroLectura, 'r')
    suma = 0
    contador = 0

    with open(ficheroLectura, 'r') as f1:
        for linea in f1.readlines():
            suma += int(linea.strip())
            contador += 1

    media = suma / contador

    f1.close()
    with lock:
        with open(ficheroEscritura, 'w') as f2:
            f2.write(f"{alumno} {media}\n")

    return (alumno, media)


def obtenerNotaMaxima(fichero):

    f = open(fichero, 'r')

    max_nota = -1
    alumno_max = ""

    with open(fichero, 'r') as f:
        for linea in f.readlines():
            alumno, nota = linea.strip().split(" ")
            nota = float(nota)
            if nota > max_nota:
                max_nota = nota
                alumno_max = alumno

    f.close()
    return (alumno_max, max_nota)


if __name__ == '__main__':

    inicio = time.time()
    alumnos = [f"Alumno{i+1}" for i in range(10)]
    ficheros_notas = [f"C:\\Users\\Usuario\\Documents\\Programacion-de-Servicios-y-Procesos\\Tema2\\Boletin2\\Alumno{i+1}.txt" for i in range(10)]
    fichero_medias = 'medias.txt'

    with Pool(processes=len(alumnos)) as pool:
        pool.map(generarNumero, ficheros_notas)

    args = list(zip(ficheros_notas, [fichero_medias]*len(alumnos), alumnos))
    with Pool(processes=len(alumnos)) as pool:
        pool.starmap(calcularMedia, args)


    with Pool(processes=1) as pool:
        resultados = pool.map(obtenerNotaMaxima, (fichero_medias,))

    alumno_max, max_nota = resultados[0]
    print(f"Alumno con la nota máxima: {alumno_max} con una nota de {max_nota}")

    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio} segundos")