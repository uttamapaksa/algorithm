function bellmanFord() {
  const INF = 5000001;
  const dist: number[] = Array(N+1).fill(INF);
  dist[1] = 0;
  
  for (let u=1; u<N+1; u++) {
    for (const [a, b, c] of graph) {
      if (dist[a] === INF) {continue}; // unreachable
      if (dist[b] > dist[a] + c) {
        dist[b] = dist[a] + c;
      }
    }
  }

  for (let u=1; u<N+1; u++) {
    for (const [a, b, c] of graph) {
      if (dist[a] === INF) {continue};
      if (dist[b] > dist[a] + c) {
        return -1 // cycle
      }
    }
  }

  let ans = "";
  for (let i=2; i<N+1; i++){
    ans += `${dist[i] === INF ? -1 : dist[i]} `;
  }
  return ans
}


const input: string[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n");
const [N, M] = input[0].split(/\s/).map(Number);
const graph: number[][] = [];
for (let i=1; i<M+1; i++) {
  graph.push(input[i].split(/\s/).map(Number));
}

console.log(bellmanFord());