function distance([x1, y1]: number[], [x2, y2]: number[]): number {
    return Math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
}


function find(x: number): number {
    if (x !== Parent[x]) {
        Parent[x] = find(Parent[x])
    }
    return Parent[x]
}


function union(x: number, y: number): void {
    const [a, b] = [find(x), find(y)]
    a < b ? Parent[b] = a : Parent[a] = b
}


const input: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number))
const [N, M] = input[0]
let ans = 0

const coordinate: Record<number, number[]> = {}
for (let i=1; i<1+N; i++) {
    coordinate[i] = input[i]
}

const Parent: number[] = Array.from({length: N+1}, (_, i) => i);
for (let i=1+N; i<1+N+M; i++) {
    const [x, y] = input[i]
    union(x, y)
}

let graph: number[][] = []
for (let i=1; i<N; i++) {
    for (let j=i+1; j<N+1; j++) {
        graph.push([distance(coordinate[i], coordinate[j]), i, j])
    }
}
graph = graph.sort((a,b)=>a[0]-b[0])

for (const [w, u, v] of graph) {
    if (find(u) !== find(v)) {
        ans += w
        union(u, v)
    }
}

console.log(ans.toFixed(2))