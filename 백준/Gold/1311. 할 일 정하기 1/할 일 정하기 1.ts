function dfs(k: number, visit: number): number {
    if (k === N[0]) return 0 // done
    if (memo[visit]) return memo[visit] // memoization
    
    let minCost = Infinity
    for (let i=0; i<N[0]; i++) {
        if (visit & 1 << i) continue // visited
        const newVisit = visit | (1 << i)
        const newCost = tasks[k][i] + dfs(k + 1, newVisit)
        minCost = Math.min(minCost, newCost);
    }

    memo[visit] = minCost
    return minCost;
}


const [N, ...tasks]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map((x:string)=>+x))
const memo: Record<number, number> = {}
console.log(dfs(0, 0))