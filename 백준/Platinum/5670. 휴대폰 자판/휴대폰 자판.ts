const input: string[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(''))
type TrieType = {[key: string]: any}
let ans = ''

let i = 0
while (i < input.length) {

  function insert(word: string[]): void {
    let node = trie
    word.forEach(char => {
      if (!node[char]) {
        node[char] = {}
      }
      node = node[char]
    })
    node['-1'] = 1
  }

  function autoComplete(word: string[]): number {
    let res = 1
    let node = trie
    word.forEach(char => {
      const keyLength = Object.keys(node[char]).length
      if (!keyLength) return res
      else if (keyLength > 1) res += 1
      node = node[char]
    })
    if (Object.keys(node).length > 1) {
      res -= 1
    }
    
    return res
  }

  const trie: TrieType = {}
  const words: string[][] = []
  const N = parseInt(input[i].join(''))
  i += 1
  for (let j=0; j<N; j++) {
    const word = input[i + j]
    insert(word)
    words.push(word)
  }
  i += N

  let total = 0
  words.forEach(word => total += autoComplete(word))
  ans += `${(total / N).toFixed(2)}\n`
}

console.log(ans)