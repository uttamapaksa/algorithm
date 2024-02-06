function furthestNode(u: number) {
  const stack: number[] = [u];
  const visit: number[] = Array(N[0]+1).fill(-1);
  visit[u] = 0;

  while (stack.length) {
    const u = stack.pop() as number;
    if (!graph[u]) continue;
    for (const [v, w] of graph[u]) {
      if (visit[v] !== -1) continue;
      stack.push(v);
      visit[v] = visit[u] + w;
    }
  }
 
  let maxd = 0;
  let maxi = 0;
  for (let i=1; i<N+1; i++) {
    if (maxd < visit[i]) {
      maxd = visit[i];
      maxi = i;
    }
  }
  return [maxd, maxi];
}


const [N, ...arr] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.trim().split(" ").map(Number));
const graph: Record<number, number[][]> = {};
for (let i=1; i<N+1; i++) {
  graph[i] = [];
}
for (const [u, v, w] of arr) {
  graph[u].push([v, w]); 
  graph[v].push([u, w]); 
}

console.log(furthestNode(furthestNode(1)[1])[0]);