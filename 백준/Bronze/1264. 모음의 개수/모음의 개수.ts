const vow = new Set('aeiouAEIOU');
const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

for (const str of input) {
  if (str === '#') break;
  const res = [...str].reduce((count, char) => count + (vow.has(char) ? 1 : 0), 0);
  console.log(res);
}