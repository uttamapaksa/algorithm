const [[xs, ys], [xe, ye], [a1, b1, c1, d1], [a2, b2, c2, d2], [a3, b3, c3, d3]]: number[][] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.split(" ").map(Number));
const index: number[][] = [[xs, ys], [a1, b1], [c1, d1], [a2, b2], [c2, d2], [a3, b3], [c3, d3], [xe, ye]];
const graph: number[][] = Array.from({length: 8}, () => Array(8).fill(0));

// all <-> all
for (let u = 0; u < 7; u++) {
    let [x1, y1] = index[u];
    for (let v = u+1; v < 8; v++) {
        let [x2, y2] = index[v];
        let diff = Math.abs(x1 - x2) + Math.abs(y1 - y2);
        graph[u][v] = diff;
        graph[v][u] = diff;
    }
}
// teleport <-> teleport
for (const [u, v] of [[1, 2], [3, 4], [5, 6]]) {
    let diff = graph[u][v];
    graph[u][v] = Math.min(diff, 10);
    graph[v][u] = Math.min(diff, 10);
}
// dijkstra
const dist = Array(8).fill(Infinity);
dist[0] = 0;
const heap: number[][] = [[dist[0], 0]];

while (heap.length) {
    const [d, u] = heap.pop() as number[];
    if (dist[u] < d) continue;
    for (let v = 0; v < 8; v++) {
        if (dist[v] > d + graph[u][v]) {
            dist[v] = d + graph[u][v];
            heap.push([dist[v], v]);
        }
    }
}
// dist[end]
console.log(dist[7]);