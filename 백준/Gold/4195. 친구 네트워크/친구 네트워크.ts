const input: any = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n")
const T: number = input[0]
let t: number = 0
let ans: string = ""

for (let _=0; _<T; _++) {
    const N: number = parseInt(input[++t])
    const P: Record<string, string> = {}
    const C: Record<string, number> = {}
    
    function find(x: string): string {
        if (x != P[x]) {
            P[x] = find(P[x])
        }
        return P[x]
    }

    function union(x: string, y: string): number {
        const [a, b] = [find(x), find(y)]
        const c = a !== b ? C[a] + C[b] : C[a]
        a < b ? P[b] = a : P[a] = b
        C[b] = C[a] = c 
        return c
    }

    for (let _=0; _<N; _++) {
        const [a, b]: string[] = input[++t].trim().split(" ")
        if (!P[a]) P[a] = a, C[a] = 1
        if (!P[b]) P[b] = b, C[b] = 1
        ans += `${union(a, b)}\n`
    }
}

console.log(ans)