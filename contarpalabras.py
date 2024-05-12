# len() -> longitud de una lista
# list() -> convierte un objeto iterable en una lista
# filter() -> filtra los elementos de una lista
# lambda -> función anónima
# split() -> separa una cadena de texto en una lista
# strip() -> elimina los espacios en blanco al principio y al final de una cadena de texto
# lambda x: x != '' -> función anónima que recibe un parámetro x y devuelve True si x es diferente de un espacio en blanco

# numero_palabras = len(list(filter(lambda x: x != '', texto.strip().split())))


texto = "          Hola, me llamo Juan        y me gusta programar en python     "

numero_palabras = len(list(filter(lambda x: x != '', texto.strip().split())))
print(f"El número de palabras en la cadena es: {numero_palabras}")