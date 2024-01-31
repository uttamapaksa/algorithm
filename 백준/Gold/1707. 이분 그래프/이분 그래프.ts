function sol(graph: Record<number, number[]>, V: number) {
  const visit: number[] = Array(V+1).fill(0);
  const stack: number[] = [];
  
  for (let u=1; u<V+1; u++) {
    if (visit[u]) continue;
    stack.push(u);

    while (stack.length > 0) {
      const s = stack.pop() as number;
      
      for (const e of graph[s]) {
        if (visit[e] === 0) {
          visit[e] = visit[s] === 1 ? 2 : 1;
          stack.push(e);
        } else if (visit[s] === visit[e]) {
          return "NO";
        }
      }
    }
  }

  return "YES";
}


const input: string[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n");
const N = parseInt(input[0])

let di = 1;
for (let i=0; i<N; i++) {
  const [V, E]: number[] = input[i+di].split(/\s/).map((x:string)=>parseInt(x));
  
  const graph: Record<number, number[]> = {};
  for (let j=1; j<V+1; j++) {
    graph[j] = [];
  }

  for (let j=1; j<E+1; j++) {
    const [a, b]: number[] = input[i+di+j].split(/\s/).map((x:string)=>parseInt(x));
    graph[a].push(b);
    graph[b].push(a);
  }
  di += E;

  console.log(sol(graph, V));
}