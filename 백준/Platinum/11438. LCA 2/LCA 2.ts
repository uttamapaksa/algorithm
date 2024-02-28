function dfs(p: number, c: number, d: number) {
  if (par[c][0]) return

  depth[c] = d
  par[c][0] = p
  for (const x of graph[c]) {
    dfs(c, x, d+1)
  }
}


function parentDP() {
  for (let j=1; j<LOG; j++) {
    for (let i=1; i<N+1; i++) {
      par[i][j] = par[par[i][j-1]][j-1]
    }
  }
}


function LCA(a: number, b: number): number {
  if (depth[a] < depth[b]) [a, b] = [b, a] // depth[a] > depth[b]
  for (let i=LOG-1; i>=0; i--) {
    if ((depth[a] - depth[b]) >= (1 << i) ) {
      a = par[a][i]
    }
  }
  
  if (a === b) {
    return a
  }
  for (let i=LOG-1; i>=0; i--) {
    if (par[a][i] !== par[b][i]) {
      a = par[a][i]
      b = par[b][i]
    }
  }
  return par[a][0]
}


const [[N], ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
const [edges, [M], queries] = [input.slice(0, N-1), input[N-1], input.slice(N)]
const LOG = 18 // 2 ** 17 > N
const graph: number[][] = Array.from({ length: N+1 }, () => [])
const par: number[][] = Array.from({ length: N+1 }, () => Array(LOG).fill(0))
edges.forEach(([u, v]) => (graph[u].push(v), graph[v].push(u)))
const depth = Array(N+1).fill(0)
dfs(1, 1, 0)
parentDP()

let ans = '';
queries.forEach(([u, v]) => ans += `${LCA(u, v)}\n`)
console.log(ans)