function insert(str: string[]) {
  let node = trie
  for (const char of str) {
    if (!node[char]) {
      node[char] = {}
    }
    node = node[char]
  }
}


function traverse(n: number, trie: TrieType): string {
  const nodes = Array.from(Object.keys(trie)).sort()
  let ans = ''
  for (const node of nodes) {
    ans += `${'--'.repeat(n)}${node}\n${traverse(n+1, trie[node])}`
  }
  return ans
}


const words: string[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').slice(1).map((x: string)=>x.trim().split(' ').slice(1))
interface TrieType { [key: string]: any }
const trie: TrieType = {}
words.forEach(word=>insert(word))

console.log(traverse(0, trie))