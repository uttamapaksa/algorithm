const nums: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
nums.pop()
nums.forEach(x => {
  const [a, b, c] = x.sort((a,b)=>b-a)
  if (a >= b+c) console.log('Invalid')
  else if (a === c) console.log('Equilateral')
  else if (a === b || b === c) console.log('Isosceles')
  else console.log('Scalene')
})