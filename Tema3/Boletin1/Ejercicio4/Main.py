from ContadorVocal import ContadorVocal

vocales = ["a", "e", "i", "o", "u"]

hilos = [ContadorVocal(vocal) for vocal in vocales]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

total = 0

for hilo in hilos:
    print(f"Vocal '{hilo.vocal}': {hilo.resultado} apariciones")
    total += hilo.resultado

print(f"Total de vocales: {total} vocales")