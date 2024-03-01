function dfs(p: number) {
  const stack = [p]
  par[p][0] = p
  while (stack.length) {
    const u = stack.pop() as number
    for (const [v, w] of graph[u]) {
    if (par[v][0]) continue
    par[v][0] = u
    cost[v][0] = w
    depth[v] = depth[u] + 1
    stack.push(v)
    }
  }
}


function parentDP() {
  for (let j=1; j<LOG; j++) {
    for (let i=1; i<=N; i++) {
      par[i][j] = par[par[i][j-1]][j-1]
      cost[i][j] = cost[i][j-1] + cost[par[i][j-1]][j-1]
    }
  }
}


function LCANodeCost(u: number, v: number) {
  let currCost = 0
  if (depth[u] < depth[v]) [u, v] = [v, u]
  for (let i=LOG-1; i>-1; i--) {
    if (depth[u] - depth[v] >= (1 << i)) {
      currCost += cost[u][i]
      u = par[u][i]
    }
  }

  if (u === v) return [u, currCost]
  for (let i=LOG-1; i>-1; i--) {
    if (par[u][i] !== par[v][i]) {
      currCost += cost[u][i]
      currCost += cost[v][i]
      u = par[u][i]
      v = par[v][i]
    }
  }
  currCost += cost[u][0]
  currCost += cost[v][0]
  return [par[u][0], currCost]
}


function LCAPath(u: number, v: number, k: number, LCA: number) {
  const UD = depth[u] - depth[LCA]
  const VD = depth[v] - depth[LCA]
  if (UD <= k) [u, k] = [v, UD + VD - k]
  for (let i=LOG-1; i>-1; i--) {
    if (k >= (1 << i)) {
      k -= (1 << i)
      u = par[u][i]
    }
  }
  return u
}


const [[N], ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
const [edges, queries] = [input.slice(0, N-1), input.splice(N)]
const LOG = 18
const graph: number[][][] = Array.from({length: N+1}, ()=>[])
edges.forEach(([u, v, w]) => (graph[u].push([v, w]), graph[v].push([u, w])))
const par: number[][] = Array.from({length: N+1}, ()=>Array(LOG).fill(0))
const cost: number[][] = Array.from({length: N+1}, ()=>Array(LOG).fill(0))
const depth: number[] = Array(N+1).fill(0)
dfs(1)
parentDP()

let ans = ''
for (const [oper, u, v, k] of queries) {
  const [LCA, LCACost] = LCANodeCost(u, v)
  if (oper === 1) ans += `${LCACost}\n`
  else ans += `${LCAPath(u, v, k-1, LCA)}\n`
}
console.log(ans)