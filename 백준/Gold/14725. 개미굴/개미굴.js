function insert(str) {
  let node = trie
  for (const char of str) {
    if (!node[char]) {
      node[char] = {}
    }
    node = node[char]
  }
}

function traverse(n, trie) {
  const nodes = Object.keys(trie).sort()
  for (const node of nodes) {
    ans += `${'--'.repeat(n)}${node}\n`
    traverse(n + 1, trie[node])
  }
}

const [_, ...__] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(x=>x.trim().split(' '))
const arr = __.map(([_, ...str]) => str)
const trie = {}; for (const str of arr) insert(str)

let ans = ''
traverse(0, trie)
console.log(ans)