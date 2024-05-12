cadena = "esto es una cadena de texto"
caracter = "e"
conteo = 0

for letra in cadena:
    if letra == caracter:
        conteo += 1

print(f'El caracter "{caracter}" se repite {conteo} veces en la cadena: "{cadena}"')