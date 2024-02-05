function furthestNode(u: number) {
  const stack: number[] = [u];
  const visit: number[] = Array(N+1).fill(-1);
  visit[u] = 0;

  while (stack.length) {
    const u = stack.pop() as number;
    for (const [v, w] of graph[u]) {
      if (visit[v] !== -1) continue;
      stack.push(v);
      visit[v] = visit[u] + w;
    }
  }

  let maxi = 0;
  let maxd = 0;
  for (let i=1; i<N+1; i++) {
    if (maxd < visit[i]) {
      maxi = i;
      maxd = visit[i];
    }
  }
  return [maxi, maxd];
}


let [N, ...arr] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.trim().split(" ").map(Number));
N = N[0];
let graph: Record<number, number[][]> = {};
let root: number;

for (let i=0; i<N; i++) {
  const row: number[] = arr[i];
  const node: number = arr[i][0];
  graph[node] = [];
  for (let j=2; j<row.length-1; j+=2) {
    graph[node].push([row[j-1], row[j]]);
  }
}

console.log(furthestNode(furthestNode(1)[0])[1]);