function kmpTable(): number[] {
  const m = pattern.length
  const table = Array(m).fill(0)
  
  let j = 0
  for (let i=1; i<m; i++) {
    while (j > 0 && pattern[i] !== pattern[j]) {
      j = table[j - 1]
    }
    if (pattern[i] === pattern[j]) {
      j += 1
    }
    table[i] = j
  }

  return table
}


function kmpSearch(): string {
  const n = text.length
  const m = pattern.length
  const table = kmpTable()
  
  let j = 0
  let cnt = 0
  let idx: number[] = []
  for (let i=0; i<n; i++) {
    while (j > 0 && text[i] !== pattern[j]) {
      j = table[j - 1]
    }
    if (text[i] === pattern[j]) {
      j += 1
      if (j === m) {
        cnt += 1
        idx.push(i - m + 2)
        j = table[j - 1]
      }
    }
  }

  let res = `${cnt}\n`
  idx.forEach((x: number) => res += `${x} `)
  return res
}


const [text, pattern]: string[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().split('\n').map((x: string)=>x.split(''))
if (text[text.length-1] === '\r') text.pop()
console.log(kmpSearch())