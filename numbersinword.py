import re # Importamos la librería re (Regular Expressions)
# findall() es una función que busca todas las ocurrencias de un patrón en un texto

texto = " adhasda6stdas7fas8f9as8f0saf87 "
numeros_encontrados = re.findall(r'\d', texto)
print(numeros_encontrados)


numero_total = len(numeros_encontrados)

print(f"El número total de números en el texto es: {numero_total}")