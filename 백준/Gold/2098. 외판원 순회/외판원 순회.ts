function dfs(k: number, prev: number, visit: number): number {
    if (k === N[0] - 1) return costs[prev][0] ? costs[prev][0] : Infinity
    if (memo[prev][visit]) return memo[prev][visit]

    let minCost = Infinity
    for (let curr = 1; curr < N[0]; curr++) {
        if (!costs[prev][curr] || visit & (1 << curr)) continue // unreachable or visited
        const newVisit = visit | (1 << curr)
        const newCost = costs[prev][curr] + dfs(k + 1, curr, newVisit)
        minCost = Math.min(minCost, newCost)
    }

    memo[prev][visit] = minCost
    return minCost
}


const [N, ...costs]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map((x:string)=>+x))
const memo: number[][] = Array.from({length: N[0]}, ()=>Array(1 << N[0]).fill(0))
console.log(dfs(0, 0, 0))