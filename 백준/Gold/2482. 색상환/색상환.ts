function dfs(n: number, k: number): number {
    if (memo[n][k]) return memo[n][k] // memoization
    if (n < 2*k) return 0

    memo[n][k] += dfs(n-2, k-1) + dfs(n-1, k)
    memo[n][k] %= 1000000003
    return memo[n][k]
}


const [N, K]: number[] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>+x)
const memo: number[][] = Array.from({length: N+1}, ()=>Array(Math.trunc(N/2)+1).fill(0)) // [n][k]
for (let i=1; i<=N; i++) memo[i][1] = i // initialization
for (let i=1; i<=Math.trunc(N/2); i++) memo[i*2][i] = 2
console.log(dfs(N, K))