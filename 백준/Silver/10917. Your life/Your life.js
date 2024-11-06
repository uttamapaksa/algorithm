function bfs() {
  let front = 0;
  while (front < queue.length) {
    const [u, cnt] = queue[front++];
    for (const v of graph[u]) {
      if (visit[v]) continue;
      if (v == N) return cnt+1
      visit[v] = 1
      queue.push([v, cnt+1]) 
    }
  }
  return -1
}

const [[N, M], ...xy] = require('fs').readFileSync(0).toString().trim().split('\n').map((x) => x.split(' ').map(Number));
const graph = Array.from({ length: N }, () => []);
const visit = Array.from({ length: N }, () => 0);
const queue = [];
for (const [x, y] of xy) {
  graph[x].push(y);
  visit[1] = 1
  queue.push([1, 0]);
}

console.log(bfs());