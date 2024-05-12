cadena = "Hola Mundo"
cadena_invertidaSlicing = cadena[::-1]
print(cadena_invertidaSlicing)  # Resultado: "odnuM aloH"

cadena_invertidaFor = ""
for caracter in cadena[::-1]: # [start:stop:step]
    cadena_invertidaFor += caracter
print(cadena_invertidaFor)  # Resultado: "odnuM aloH"


cadena_invertidaM = ''.join(reversed(cadena))
print(cadena_invertidaM)  # Resultado: "odnuM aloH"


# "rebanado inverso" o "slicing inverso".
# Técnica que te permite extraer parte de una secuencia (como una cadena de texto, lista o tupla) utilizando una notación especial [start:stop:step].
# start: Índice de inicio de la rebanada (inclusive).
# stop: Índice de fin de la rebanada (exclusivo).
# step: Tamaño del paso para la rebanada (puede ser negativo para rebanar en reversa).