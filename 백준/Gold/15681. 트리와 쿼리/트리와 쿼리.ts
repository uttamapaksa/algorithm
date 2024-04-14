function dfs(u: number): number {
    visit[u] = 1
    for (const v of graph[u]) {
        if (!visit[v]) {
            visit[u] += dfs(v)
        }
    }
    return visit[u]
}


const input: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number))
const [N, R, Q] = input[0]
const visit: number[] = Array(N+1).fill(0)
const graph: Record<number, number[]> = {}
for (let i=1; i<N+1; i++) {
    graph[i] = []
}
for (let i=1; i<N; i++) {
    const [u, v] = input[i]
    graph[u].push(v)
    graph[v].push(u)
}
dfs(R)


let ans = ''
for (let i=N; i<N+Q; i++) {
    ans += `${visit[input[i][0]]}\n`
}
console.log(ans)