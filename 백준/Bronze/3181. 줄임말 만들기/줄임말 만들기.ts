const ignore: Set<string> = new Set<string>(['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']);
const input: string[] = require('fs').readFileSync(0).toString().trim().split(' ');
const ans: string[] = [input[0][0].toUpperCase()];
for (let i=1; i<input.length; i++) {
  if (!ignore.has(input[i])) {
    ans.push(input[i][0].toUpperCase());
  }
}
console.log(ans.join(''));