function dfs(u: number) {
    visit[u] = 1
    for (const v of graph[u]) {
        if (visit[v]) continue
        dfs(v)
        dp[u][0] += dp[v][1]
        dp[u][1] += Math.max(...dp[v])
    }
}
        

const [N, W, ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number))
const dp: number[][] = Array.from({ length: N[0]+1 }, (_, i) => [W[i-1], 0]) // add, pass
const visit: number[] = Array(N[0]+1).fill(0)
const graph: Record<number, number[]> = {}
for (let i=1; i<N[0]+1; i++) {
    graph[i] = []
}
for (const [u, v] of input) {
    graph[u].push(v)
    graph[v].push(u)
}

dfs(1)
console.log(Math.max(...dp[1]))