function dfs(u: number, d: number) {
  const stack = [[u, d]]
  par[0][u] = u
  depth[u] = d
  while (stack.length) {
    const [u, d] = stack.pop() as number[]
    for (const [v, vw] of graph[u]) {
      if (par[0][v]) continue
      par[0][v] = u
      minw[0][v] = vw
      maxw[0][v] = vw
      depth[v] = d+1
      stack.push([v, depth[v]])
    }
  }
}


function parentDP() {
  for (let j=1; j<LOG; j++) {
    for (let i=1; i<N+1; i++) {
      par[j][i] = par[j-1][par[j-1][i]]
      minw[j][i] = Math.min(minw[j-1][i], minw[j-1][par[j-1][i]])
      maxw[j][i] = Math.max(maxw[j-1][i], maxw[j-1][par[j-1][i]])
    }
  }
}


function LCA(a: number, b: number): string {
  if (a === b) {
    return '0 0'
  }
  
  let minv = 1000000, maxv = 0
  if (depth[a] < depth[b]) [a, b] = [b, a] // depth[a] > depth[b]
  for (let i=LOG-1; i>=0; i--) {
    if ((depth[a] - depth[b]) >= (1 << i) ) {
      minv = Math.min(minv, minw[i][a])
      maxv = Math.max(maxv, maxw[i][a])
      a = par[i][a]
    }
  }
  
  if (a === b) {
    return `${minv} ${maxv}`
  }
  for (let i=LOG-1; i>=0; i--) {
    if (par[i][a] !== par[i][b]) {
      minv = Math.min(minv, minw[i][a], minw[i][b])
      maxv = Math.max(maxv, maxw[i][a], maxw[i][b])
      a = par[i][a]
      b = par[i][b]
    }
  }
  minv = Math.min(minv, minw[0][a], minw[0][b])
  maxv = Math.max(maxv, maxw[0][a], maxw[0][b])
  return `${minv} ${maxv}`
}


const [[N], ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
const [edges, K, queries] = [input.slice(0, N-1), input[N-1][0], input.slice(N)]
const graph: number[][][] = Array.from({ length: N+1 }, () => [])
edges.forEach(([u, v, w]) => (graph[u].push([v, w]), graph[v].push([u, w])))
const LOG = 18 // 2 ** 17 > N
const par: number[][] = Array.from({ length: LOG }, () => Array(N+1).fill(0))
const minw: number[][] = Array.from({ length: LOG }, () => Array(N+1).fill(1000000))
const maxw: number[][] = Array.from({ length: LOG }, () => Array(N+1).fill(0))
const depth = Array(N+1).fill(0)
dfs(1, 0)
parentDP()

console.log(queries.reduce((a, [u, v]) => a + LCA(u, v) + '\n', ''))