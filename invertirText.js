let cadena = "Hola Mundo";

let textInvertMethod = cadena.split("").reverse().join("");
console.log(textInvertMethod); // Resultado: "odnuM aloH"

let textInvertFor = "";
for (let i = cadena.length - 1; i >= 0; i--) {
  textInvertFor += cadena[i];
  console.log(textInvertFor);
}
console.log(textInvertFor); // Resultado: "odnuM aloH"
