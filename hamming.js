let text1 = "GATTACA";
let text2 = "GACTATA";
let dist = 0;

if (text1.length !== text2.length) {
  throw new Error(
    "Las cadenas deben tener la misma longitud para calcular la distancia de Hamming."
  );
}

for (let i = 0; i < text1.length; i++) {
  if (text1[i] !== text2[i]) {
    dist++;
  }
}

console.log(`el text1 del tex2 difieren en ${dist} caracteres`);
