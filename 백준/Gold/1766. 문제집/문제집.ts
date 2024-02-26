function solve(u: number): void {
  for (let v = 1; v <= u; v++) {
    if (indegree[v]) continue
    indegree[v] = -1 // visit
    ans += `${v} `
    
    for (const w of graph[v]) {
      indegree[w] -= 1
    }
  
    solve(v)
  }
}

const input = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number))
const [N, M] = input[0]
const graph: Record<number, number[]> = {}; for (let i=1; i<=N; i++) graph[i] = []
const indegree: number[] = Array(N+1).fill(0)
let ans = ''
let minv = 1

for (let i=1; i<=M; i++) {
  const [u, v] = input[i]
  graph[u].push(v)
  indegree[v] += 1
}

solve(N)
console.log(ans)