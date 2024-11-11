const [[N, M], ...ipt] = require('fs').readFileSync(0).toString().trim().split('\n').map(x => x.split(' ').map(Number))
const graph = Array.from({length: N+1}, ()=>Object())
for (let i=0; i<N-1; i++) {
  const [u, v, d] = ipt[i]  
  graph[u][v] = d
  graph[v][u] = d
}

const par = Array.from({length: N+1}, (_,i)=>i)
const depth = Array(N+1).fill(-1)
depth[1] = 0
const stack = [1]
while (stack.length) {
  const u = stack.pop()
  for (let v in graph[u]) {
    v = parseInt(v)
    if (depth[v] !== -1) continue
    par[v] = u
    depth[v] = depth[u] + 1
    stack.push(v)
  }
}

for (let i=N-1; i<N+M-1; i++) {
  let res = 0
  let [u, v] = ipt[i]
  if (depth[u] !== depth[v]) {
    if (depth[u] > depth[v]) {
      [u, v] = [v, u]
    }
    const diff = depth[v]-depth[u]
    for (let j=0; j<diff; j++) {
      res += graph[v][par[v]]
      v = par[v]
    }
  }
  
  while (u !== v) {
    res += graph[u][par[u]]
    u = par[u]
    res += graph[v][par[v]]
    v = par[v]
  }
  console.log(res)
}