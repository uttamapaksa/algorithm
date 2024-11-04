const input = require('fs').readFileSync(0).toString().trim()
const suf = []
for (let i=0; i<input.length; i++) {
  suf.push(input.slice(i))
}
console.log(suf.sort().join('\n'));