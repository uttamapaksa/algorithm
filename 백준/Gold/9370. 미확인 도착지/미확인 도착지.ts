function sol(graph: Record<number, number[][]>, [n, s]: number[]) {
  const dist: number[] = Array(n+1).fill(2000001);
  dist[s] = 0;
  let priorityStack: number[][] = [[dist[s], s]];

  while (priorityStack.length > 0) {
    priorityStack = priorityStack.sort((a, b) => b[0] - a[0]);
    const [d, u] = priorityStack.pop() as number[];

    if (dist[u] < d) continue;
    for (const [w, v] of graph[u]) {
      if (dist[v] > d + w) {
        dist[v] = d + w;
        priorityStack.push([dist[v], v])
      }
    }
  }

  return dist
}


const input: string[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n");
const N = parseInt(input[0])

let di = 1;
for (let i=0; i<N; i++) {
  const [n, m, t]: number[] = input[i+di].split(/\s/).map((x:string)=>parseInt(x));
  const [s, g, h]: number[] = input[i+di+1].split(/\s/).map((x:string)=>parseInt(x));
  di += 1;
  
  const graph: Record<number, number[][]> = {};
  for (let j=1; j<n+1; j++) {
    graph[j] = [];
  }
  for (let j=1; j<m+1; j++) {
    const [a, b, d]: number[] = input[i+di+j].split(/\s/).map((x:string)=>parseInt(x));
    graph[a].push([d, b]);
    graph[b].push([d, a]);
  }
  di += m;

  let destinations: number[] = [];
  for (let j=1; j<t+1; j++) {
    destinations.push(parseInt(input[i+di+j]));
  }
  destinations = destinations.sort((a,b)=>a-b);
  di += t;


  const dists = sol(graph, [n, s]);
  const distg = sol(graph, [n, g]);
  const disth = sol(graph, [n, h]);
  let w = (graph[g].find(x => x[1] === h) as number[])[0];
  let ans = "";
  for (const x of destinations) {
    if (dists[x] === dists[g] + w + disth[x] || dists[x] === dists[h] + w + distg[x]) {
      ans += `${x} `
    }
  }
  console.log(ans);
}