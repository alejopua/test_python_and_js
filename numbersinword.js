let text = " adhasda6stdas7fas8f9as8f0saf87 ";
let nNumbers = text.match(/\d+/g);

let totalNumbers = nNumbers ? nNumbers.length : 0;

console.log(`Number of numbers is: ${totalNumbers}`);
