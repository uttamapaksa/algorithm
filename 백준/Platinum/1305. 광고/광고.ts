function kmpTable(): number {
  const m = text.length
  const table = Array(m).fill(0)
  
  let j = 0
  for (let i=1; i<m; i++) {
    while (j > 0 && text[i] !== text[j]) {
      j = table[j - 1]
    }
    if (text[i] === text[j]) {
      j += 1
    }
    table[i] = j
  }

  return table[m-1]
}


const [_, text]: string[] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n')
const N = parseInt(_)
console.log(N - kmpTable())