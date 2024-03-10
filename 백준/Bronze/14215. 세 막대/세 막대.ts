const nums: number[] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split(' ').map(Number)
const [a, b, c] = nums.sort((a,b)=>b-a)
console.log(a >= b+c ? 2 * (b+c) - 1 : a + b + c)