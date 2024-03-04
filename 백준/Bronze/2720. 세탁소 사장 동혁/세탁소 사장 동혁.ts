const [_, ...coins]: number[] =require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(Number)
let ans = ''; const div = [25, 10, 5]
coins.forEach((coin) => {for (let i=0; i<3; i++) {ans += `${Math.trunc(coin / div[i])} `; coin %= div[i]} ans += `${coin}\n`})
console.log(ans)