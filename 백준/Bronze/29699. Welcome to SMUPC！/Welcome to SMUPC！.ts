const word = "CWelcomeToSMUP";
const N: number = +require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim()
console.log(word[N%14]);