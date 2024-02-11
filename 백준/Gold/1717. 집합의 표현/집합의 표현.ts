function find(x: number): number {
    if (x != P[x]) {
        P[x] = find(P[x])
    }
    return P[x]
}


function union(x: number, y: number): void {
    const [a, b] = [find(x), find(y)]
    a < b ? P[b] = a : P[a] = b
}


const [nums, ...arr]: number[][] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.split(" ").map(Number))
const P: number[] = Array.from({length: nums[0]+1}, (_, i) => i)
let ans = ""
for (const [oper, a, b] of arr) {
    oper ? find(a) === find(b) ? ans += "YES\n" : ans += "NO\n" : union(a, b)
}
console.log(ans)