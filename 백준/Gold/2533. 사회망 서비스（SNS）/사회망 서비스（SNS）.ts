function dfs(u: number): number {
    visit[u] = 1
    for (const v of graph[u]) {
        if (visit[v]) continue
        if (dfs(v) === 1) visit[u] = 2
    }
    if (visit[u] === 2) ans += 1
    return visit[u]
}
        

const [N, ...edges]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number))
const visit: number[] = Array(N[0]+1).fill(0)
const graph: Record<number, number[]> = {}
for (let i=1; i<N[0]+1; i++) graph[i] = []
for (const [u, v] of edges) graph[u].push(v), graph[v].push(u)

let ans = 0
dfs(1)
console.log(ans)