text1 = "GATTACA";
text2 = "GACTATA";
dist = 0;

if len(text1) != len(text2):
  raise ValueError("Las cadenas deben tener la misma longitud para calcular la distancia de Hamming.")


for i in range(len(text1)): 
  if text1[i] != text2[i]:
    dist += 1;

print(f"el text1 del tex2 difieren en {dist} caracteres.");