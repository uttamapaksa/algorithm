function dfs(p: number, d: number) {
  const stack = [[p, d]]
  depth[p] = d
  par[0][p] = p
  while (stack.length) {
    const [p, d] = stack.pop() as number[]
    for (const c of graph[p]) {
      if (par[0][c]) continue
      depth[c] = d+1
      par[0][c] = p
      stack.push([c, d+1])
    }
  }
}


function parentDP() {
  for (let j=1; j<LOG; j++) {
    for (let i=1; i<N+1; i++) {
      par[j][i] = par[j-1][par[j-1][i]]
    }
  }
}


function LCA(a: number, b: number): number {
  if (depth[a] < depth[b]) [a, b] = [b, a] // depth[a] > depth[b]
  for (let i=LOG-1; i>=0; i--) {
    if ((depth[a] - depth[b]) >= (1 << i) ) {
      a = par[i][a]
    }
  }
  
  if (a === b) {
    return a
  }
  for (let i=LOG-1; i>=0; i--) {
    if (par[i][a] !== par[i][b]) {
      a = par[i][a]
      b = par[i][b]
    }
  }
  return par[0][a]
}


const [[N], ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
const [edges, [M], queries] = [input.slice(0, N-1), input[N-1], input.slice(N)]
const graph: number[][] = Array.from({ length: N+1 }, () => [])
edges.forEach(([u, v]) => (graph[u].push(v), graph[v].push(u)))
const LOG = 18 // 2 ** 17 > N
const par: number[][] = Array.from({ length: LOG }, () => Array(N+1).fill(0))
const depth = Array(N+1).fill(0)
dfs(1, 0)
parentDP()

let ans = '';
queries.forEach(([u, v]) => ans += `${LCA(u, v)}\n`)
console.log(ans)