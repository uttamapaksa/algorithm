function dfs(u: number) {
    visit[u] = 1
    for (const v of graph[u]) {
        if (visit[v]) continue
        dfs(v)
        dp[u][0] += dp[v][1] // add
        dp[u][2] = dp[u][2].concat(dp[v][3]) // add_path
        dp[u][1] += dp[v][0] > dp[v][1] ? dp[v][0] : dp[v][1] // pass
        dp[u][3] = dp[u][3].concat(dp[v][0] > dp[v][1] ? dp[v][2] : dp[v][3]) // pass_path
    }
}
        

var [N, W, ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number))
var dp: [number, number, number[], number[]][] = Array.from({ length: N[0]+1 }, (_, i) => [W[i-1], 0, [i], []]) // add, pass, add_path, pass_path
var visit: number[] = Array(N[0]+1).fill(0)
var graph: Record<number, number[]> = {}
for (let i=1; i<N[0]+1; i++) graph[i] = []
for (const [u, v] of input) graph[u].push(v), graph[v].push(u)

dfs(1)
const idx = Number(dp[1][0] < dp[1][1])
console.log(`${dp[1][idx]}\n${(dp[1][idx+2] as number[]).sort((a,b)=>a-b).join(' ')}`)