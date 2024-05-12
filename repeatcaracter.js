// Cuantas veces se repite un carácter en una cadena

let chain = "esto es una cadena de texto";
let character = "e";
let count = 0;

for (let i = 0; i < chain.length; i++) {
  if (chain[i] === character) {
    count++;
  }
}

console.log(
  `El caracter "${character}" se repite ${count} veces en la cadena: "${chain}"`
);
