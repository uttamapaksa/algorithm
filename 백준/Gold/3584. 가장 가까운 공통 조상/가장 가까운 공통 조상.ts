const [[T], ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
const LOG = 15 // 2^14 > N
let ans = ''

let i = 0
for (let _=0; _<T; _++) {
  
  function dfs(p: number, d: number) {
    depth[p] = d
    for (const x of graph[p]) {
      dfs(x, d+1)
    }
  }

  function parentDP() {
    for (let j=1; j<LOG; j++) {
      for (let i=1; i<N+1; i++) {
        parent[i][j] = parent[parent[i][j-1]][j-1]
      }
    }
  }

  function LCA(a: number, b: number): number {
    
    depth[a] >= depth[b] ? 0 : [a, b] = [b, a] // depth[a] > depth[b]
    for (let i=LOG-1; i>=0; i--) {
      if ((depth[a] - depth[b]) >= (1 << i) ) {
        a = parent[a][i]
      }
    }

    if (a === b) {
      return a
    }
    for (let i=LOG-1; i>=0; i--) {
      if (parent[a][i] !== parent[b][i]) {
        a = parent[a][i]
        b = parent[b][i]
      }
    }
    return parent[a][0]
  }
  
  const [[N], ...edges] = input.slice(i, i + 1 + input[i][0]) // slice(i, i + 1 + N)
  const [a, b] = edges.pop() as number[]
  const graph: number[][] = Array.from({ length: N+1 }, () => [])
  const parent = Array.from({ length: N+1 }, () => Array(LOG).fill(0))
  edges.forEach(([A, B]) => (graph[A].push(B), parent[B][0] = A))
  const root = parent.findIndex((v, i) => i && !v[0])
  const depth = Array(N+1).fill(0)
  dfs(root, 0)
  parentDP()
  ans += `${LCA(a, b)}\n`

  i += 1 + N
}

console.log(ans)