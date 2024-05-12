let text =
  "          Hola, me llamo Juan        y me gusta programar en javascript     ";

let cleanText = text.replace(/\s+/g, " ").trim().split(" ");
console.log(cleanText);
let nWords = cleanText.length;

console.log(`Number of words is: ${nWords}`);

// n$	Matches any string with n at the end of it
// ^n   Matches any string with n at the beginning of it
