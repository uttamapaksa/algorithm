const [T, ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
let ans = ''

let i = 0
for (let _=0; _<T[0]; _++) {
  const N = input[i][0]
  const arr = input[i+1]
  const M = input[i+2][0]
  const edges = input.slice(i+3, i+3+M);
  const rank: number[] = []
  arr.forEach((num, i) => rank[num-1] = i) // order by rank -> number
  const new_rank: number[] = Array.from(rank)
  edges.forEach(([u, v]) => {
    if (rank[u-1] > rank[v-1]) new_rank[u-1] -= 1, new_rank[v-1] += 1
    else new_rank[u-1] += 1, new_rank[v-1] -= 1
  })
  
  const tmp: number[] = []
  new_rank.forEach((num, i) => tmp[num] = i+1) // order by number -> rank
  if (new Set(new_rank).size !== N) ans += `IMPOSSIBLE\n`
  else ans += `${tmp.join(' ')}\n` 
  
  i += 3+M
}

console.log(ans)